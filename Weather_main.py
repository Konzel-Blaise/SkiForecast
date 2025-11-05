#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 21:05:57 2025
@author: blazer
This code grabs weather info from NOAA and displays it.
"""

# /zones/{type}/{zoneId}/forecast
# https://api.weather.gov/points/47.97,-120.17


import requests
import display as dis
from datetime import datetime
import time            #used for looping once/min
import pandas as pd

# Coordinates for Chelan County, WA (approx near Wenatchee)
# latitude = 47.97
# longitude = -120.17

#Stevens Pass
latitude = 47.739498
longitude = -121.094576

#Paradise

#Olympics

#North Cascades

#Alpental


# Base headers required by NOAA API
headers = {
    "User-Agent": "MSkiForecastApp (myemail@example.com)"  
}

# Step 1: Get grid information for this point
points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
points_response = requests.get(points_url, headers=headers)
points_data = points_response.json()

# Extract grid info
grid_id = points_data["properties"]["gridId"]
grid_x = points_data["properties"]["gridX"]
grid_y = points_data["properties"]["gridY"]

print(f"Using grid: {grid_id} {grid_x},{grid_y}")

# Step 2: Get the hourly forecast for that grid
forecast_url = f"https://api.weather.gov/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast/hourly"
forecast_response = requests.get(forecast_url, headers=headers)
forecast_data = forecast_response.json()

# Step 3: Print the next 12 hours of forecast
periods = forecast_data["properties"]["periods"][:24]

print(periods)

weather_data = []
#forming df
for i, period in enumerate(periods):
    dt = datetime.fromisoformat(period["startTime"])            #expand
    entry = {
        # "startTime": period["startTime"][0:13],
        "date_f": pd.to_datetime(period["startTime"][0:10]).strftime("%A - %b %-d"),
        "time_f": dt.strftime("%H"),
        "temperature": period["temperature"],
        "isDaytime": period["isDaytime"],
        "dewpoint": round(period['dewpoint']['value']),  # deg C   #rounding
        "relativeHumidity": period['relativeHumidity']['value'],
        "temp_unit": period["temperatureUnit"],
        "short_forecast": period["shortForecast"],
        "wind": period["windSpeed"],
        "windDirection": period["windDirection"],
        "precip": period['probabilityOfPrecipitation']['value']
    }
    weather_data.append(entry)
#send weather_data to df
df = pd.DataFrame(weather_data)

print(df)
#calling display func
dis.display_text(df)

time.sleep(10)



    