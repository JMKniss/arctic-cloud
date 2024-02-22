# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:09:24 2024

@author: jaymi
"""

import ephem

def get_twilight_time(latitude, longitude, date, twilight_degrees):
    obs = ephem.Observer()
    obs.lat = str(latitude)
    obs.lon = str(longitude)
    obs.date = date

    sun = ephem.Sun()
    sun.compute(obs)
    
    # Compute the twilight angle
    twilight = ephem.degrees(str(twilight_degrees))
    
    # Compute the previous and next sunset
    sunset_prev = obs.previous_setting(sun)
    sunset_next = obs.next_setting(sun)
    
    # Compute the previous and next sunrise
    sunrise_prev = obs.previous_rising(sun)
    sunrise_next = obs.next_rising(sun)
    
    # Adjust for twilight
    twilight_time_prev = obs.previous_rising(sun, start=sunset_prev, use_center=True)
    twilight_time_next = obs.next_rising(sun, start=sunset_next, use_center=True)

    obs.date = twilight_time_prev
    sun.compute(obs)
    while sun.alt > twilight:
        obs.date -= ephem.minute
        sun.compute(obs)
    twilight_time_prev = obs.date.datetime()
    
    obs.date = twilight_time_next
    sun.compute(obs)
    while sun.alt < twilight:
        obs.date += ephem.minute
        sun.compute(obs)
    twilight_time_next = obs.date.datetime()
    
    return twilight_time_prev, twilight_time_next

# Example usage
latitude = '37.7749'  # Latitude of San Francisco
longitude = '-122.4194'  # Longitude of San Francisco
date = '2024/2/22'  # Date
twilight_degrees = -15  # Twilight angle

twilight_time_prev, twilight_time_next = get_twilight_time(latitude, longitude, date, twilight_degrees)
print("Previous Twilight Time:", twilight_time_prev)
print("Next Twilight Time:", twilight_time_next)