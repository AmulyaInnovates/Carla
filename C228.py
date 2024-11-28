
import glob
import os
import sys
import time
import csv

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

actor_list = []
vehicle_control= []
#define vehicle_control variable as list
read_csv =open('manual_control_data.csv' , 'r')
reader= csv.reader(read_csv)
next(reader)
for row in reader:
	vehicle_control.append(row)
#write the code of fuction by pressing ENTER end of this sentence to avoid indentation error.


try:
    client = carla.Client('127.0.0.1', 2000)
    client.set_timeout(2.0)
    world = client.get_world()
    get_blueprint_of_world = world.get_blueprint_library()
    car_model = get_blueprint_of_world.filter('crossbike')[0]
    spawn_point = world.get_map().get_spawn_points()[1]
    dropped_vehicle = world.spawn_actor(car_model, spawn_point)


    simulator_camera_location_rotation = carla.Transform(spawn_point.location, spawn_point.rotation)
    simulator_camera_location_rotation.location += spawn_point.get_forward_vector() * 30
    simulator_camera_location_rotation.rotation.yaw += 180
    simulator_camera_view = world.get_spectator()
    simulator_camera_view.set_transform(simulator_camera_location_rotation)
    dropped_vehicle.set_transform(spawn_point)
    actor_list.append(dropped_vehicle)

    #write the code of fuction by pressing ENTER end of this sentence to avoid indentation error.
    def throttle_vehicle():
    	for vehicle_control_data in vehicle_control:
    		dropped_vehicle.apply_control(carla.VehicleControl(throttle= float(vehicle_control_data[2]) , steer= float(vehicle_control_data[3]) ,brake= float(vehicle_control_data[0])))
    		print(vehicle_control_data[2],vehicle_control_data[3],vehicle_control_data[0])
    		time.sleep(15/1000)

    throttle_vehicle()
    time.sleep(1000)
finally:
    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')