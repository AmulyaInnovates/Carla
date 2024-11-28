import glob
import os
import sys
import time
import threading

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

actor_list = []

def turn_to_right():
    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.5, steer=0.21))
    time.sleep(5)
    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.18, steer=0.25))
    time.sleep(1)
    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.34))
    time.sleep(4)


def check_traffic_lights():
    threading.Timer(0.1, check_traffic_lights).start()
    traffic_light = dropped_vehicle.get_traffic_light()

    if dropped_vehicle.is_at_traffic_light():
        print(traffic_light.get_state())

        # Task 01: Get the red light timing
        if traffic_light.get_state() == carla.TrafficLightState.Red:
            red_time = traffic_light.get_red_time()
            print(f"Red light timing: {red_time}")

        # Task 02: Change traffic light from red to yellow
        elif traffic_light.get_state() == carla.TrafficLightState.Yellow:
            traffic_light.set_state(carla.TrafficLightState.Yellow)

        # Task 03: Turn the car to the right if the traffic light color is Yellow
        if traffic_light.get_state() == carla.TrafficLightState.Yellow:
            # Turn the car to the right
            dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.3, steer=0.15))
            time.sleep(5)

            # Keep on the same lane
            dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.1, steer=0.1))
            time.sleep(1)

            # Drive straight
            dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.34))

    else:
        dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.51))

        
try:
    client = carla.Client('127.0.0.1', 2000)
    client.set_timeout(10.0)
    world = client.get_world()

    get_blueprint_of_world = world.get_blueprint_library()
    car_model = get_blueprint_of_world.filter('model3')[0]
    spawn_point = (world.get_map().get_spawn_points()[20])
    dropped_vehicle = world.spawn_actor(car_model, spawn_point)

    simulator_camera_location_rotation = carla.Transform(spawn_point.location, spawn_point.rotation)
    simulator_camera_location_rotation.location += spawn_point.get_forward_vector() * 30
    simulator_camera_location_rotation.rotation.yaw += 180
    simulator_camera_view = world.get_spectator()
    simulator_camera_view.set_transform(simulator_camera_location_rotation)
    actor_list.append(dropped_vehicle)

    # car_control()
    check_traffic_lights()
    time.sleep(1000)
finally:
    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')
