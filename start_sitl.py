# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:11:52 2022

@author: DASilva
"""

#%% start SITL
from dronekit_sitl import SITL, start_default

sitl = SITL()

#%%
sitl.download("copter", version="3.3", verbose=True)

#%%
sitl.launch([], await_ready=True, restart=True, verbose=True)
connection_string = sitl.connection_string()


#%%
print(connection_string)
# %%
