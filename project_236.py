import glob
import os
import sys
import time
import random
import math

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

actor_list = []

def generate_lidar_blueprint(blueprint_library):
    lidar_sensor = blueprint_library.filter('sensor.lidar.ray_cast_semantic')[0]
    lidar_sensor.set_attribute('channels', str(64))
    lidar_sensor.set_attribute('rotation_frequency', str(40))
    lidar_sensor.set_attribute('points_per_second', str(56000))
    lidar_sensor.set_attribute('range', str(100))
    return lidar_sensor
 
object_id = {"None": 0,
             "Buildings": 1,
             "Fences": 2,
             "Other": 3,
             "Pedestrians": 4,
             "Poles": 5,
             "RoadLines": 6,
             "Roads": 7,
             "Sidewalks": 8,
             "Vegetation": 9,
             "Vehicles": 10,
             "Wall": 11,
             "TrafficsSigns": 12,
             "Sky": 13,
             "Ground": 14,
             "Bridge": 15,
             "RailTrack": 16,
             "GuardRail": 17,
             "TrafficLight": 18,
             "Static": 19,
             "Dynamic": 20,
             "Water": 21,
             "Terrain": 22
             }

key_list = list(object_id.keys())
value_list = list(object_id.values())

def semantic_lidar_data(point_cloud_data):
    for detection in point_cloud_data:
        position = value_list.index(detection.object_tag)
        distance = math.sqrt((detection.points.x ** 2) + (detection.points.y ** 2) + (detection.points.z ** 2))
        distance_name_data = {'distance': distance, 'name': key_list[position]}
        if distance_name_data['name'] == 'Vehicles':
            print(distance_name_data)

def car_control():
    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.51))
    time.sleep(20)

try:
    client = carla.Client('127.0.0.1', 2000)
    client.set_timeout(10.0)
    world = client.get_world()
    map = world.get_map()
    get_blueprint_of_world = world.get_blueprint_library()
    car_model = get_blueprint_of_world.filter('model3')[0]
    spawn_point = (world.get_map().get_spawn_points()[6])
    dropped_vehicle = world.spawn_actor(car_model, spawn_point)

    mustang_car_blueprint = get_blueprint_of_world.filter('mustang')[0]
    mustang_car_spawn_point = (world.get_map().get_spawn_points()[4])  # set spawn point here
    mustang_car = world.spawn_actor(mustang_car_blueprint, mustang_car_spawn_point)
    mustang_car.apply_control(carla.VehicleControl(throttle=0.5))

    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.5))
    simulator_camera_location_rotation = carla.Transform(spawn_point.location, spawn_point.rotation)
    simulator_camera_location_rotation.location += spawn_point.get_forward_vector() * 30
    simulator_camera_location_rotation.rotation.yaw += 180
    simulator_camera_view = world.get_spectator()
    simulator_camera_view.set_transform(simulator_camera_location_rotation)
    actor_list.append(dropped_vehicle)

    lidar_sensor = generate_lidar_blueprint(get_blueprint_of_world)
    sensor_lidar_spawn_point = carla.Transform(carla.Location(x=0, y=0, z=2.0),
                                               carla.Rotation(pitch=0.000000, yaw=90.0, roll=0.000000))
    sensor = world.spawn_actor(lidar_sensor, sensor_lidar_spawn_point, attach_to=dropped_vehicle)

    sensor.listen(lambda point_cloud_data: semantic_lidar_data(point_cloud_data))
    car_control()

    time.sleep(1000)
finally:
    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')
