# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 01:56:13 2020

@author: TRANG THOMAS
"""
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Hour (0 to 24)':10, 'Temperature (°C)':10, 'Humidity (%)':60,'Wind Speed (m/s)':3,
                            'Visibility (10m)':1000
                            ,'Solar radiation (MJ/m2)':0,'Rainfall (mm)':0,'Snowfall (cm)':2,'Month':12
                            ,'WeekDay (1 to 7)': 1 })

print(r.json())