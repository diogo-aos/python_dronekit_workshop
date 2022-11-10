# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:12:34 2022

@author: DASilva
"""

#%%
from dronekit import connect, VehicleMode, LocationGlobal
import time

connection_string = 'tcp:127.0.0.1:5760'

#%% connect to sitl

vehicle = connect(connection_string, wait_ready=True)

#%%
speed = vehicle.airspeed

print(speed)
print(vehicle.mode)

#%%
print(vehicle.location.global_frame)

#%%

vehicle.armed

#%% GUIDED arm

vehicle.mode = VehicleMode("GUIDED")
vehicle.arm(wait=True)


#%%


#%%
vehicle.arm()
while not vehicle.armed:
    print('waiting for armed')
    time.sleep(1)
vehicle.simple_takeoff()


#%%

a_location = LocationGlobal(-34.364114, 149.166022, 30)
print(a_location)

#%%  goto command

vehicle.simple_goto(a_location, airspeed=10)



#%%
vehicle.mode = VehicleMode("GUIDED")
print(vehicle.mode)



#%%
import datetime
def observer(var):
    print(datetime.datetime.now(), var)

vehicle.add_attribute_listener("Vehicle.armed", observer)


#%%
print(vehicle.battery)