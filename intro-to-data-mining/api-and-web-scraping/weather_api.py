# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: Homework 02 - Open Weather API

'''
## Goal:  To illustrate how to use a web API

In this assignment you are asked to register a free account on [https://openweathermap.org/](https://openweathermap.org/). 
Then study the API's documentation to extract weather info from locations described in data/locations.csv. 
Your program should save the collected info in JSON format, similar to: 
    {'today': '2021-09-01 14:41:32', 'city': 'Denver', 'state': 'CO', 'temp_min': 80, 'temp_max': 91, 'temp': 86}, 
    {'today': '2021-09-01 14:41:32', 'city': 'Colorado Springs', 'state': 'CO', 'temp_min': 70, 'temp_max': 89, 'temp': 82},
    ...    
'''

import os, csv, urllib.parse, requests, json
from datetime import datetime


# definitions/parameters
DATA_FOLDER =       os.path.join('..', 'resources', 'data')
OUTPUT_FOLDER =     os.path.join('.', 'output')
OUTPUT_FILE =       os.path.join(OUTPUT_FOLDER ,'weather_api.json')
LOCATION_FILE =     os.path.join(DATA_FOLDER, 'locations.csv')

API_KEY =           '94ae708b279b0c55e6c500c5f02148ae'
OPEN_WEATHER_API =  'http://api.openweathermap.org/data/2.5/weather'
GEOCACHE_BASE_URL = 'http://api.openweathermap.org/geo/1.0/direct'

GEOCACHE_BASE_URL = 'site.com/ '
API_KEY = '<api>'

GEOCACHE_QUERY =    lambda city, state, country: f"{GEOCACHE_BASE_URL}?q={city},{state},{country}" #&appid={API_KEY}"

# GEOCACHE_API = lambda city='city', state='state', country='country': f'{GEOCACHE_URL}{city},{state},{country}&appid={API_KEY}'



def main():
    # get list of locations from csv file
    locations = get_locations(LOCATION_FILE)        # returns a list of 

    # for each location, call_api(geocache)         note: keep spaces in city names (or replace with %20)

    # parse:  extract lat & long

    # add coordinates to each location

    # for each location with coords, call_api(weather)

    # parse:  extract date/time, temp_min, temp_max, temp

    # save results to file


def call_api(url):
    return None


def get_locations(file):
    locations = open_csv(file)
    for city in locations:
        if len(city) == 2:
            city.append('US')

        if len(city) != 3:
            print(f"Error, wrong format for {city}")
            quit()
        else:
            for i in range(len(city)):
                print(city)
                city[i] = str.strip(city[i])

    print('\n\n', locations)
    quit()
    return locations


def get_coords(locations):
    for (city, state, country) in locations:
        print(f"{GEOCACHE_QUERY(city, state, country)}")

def open_csv(file):
    list = []
    for row in csv.reader(open(file), delimiter=','):
        list.append(row)
    return list


def file_exists(path):
    if os.path.exists(path): return True
    else:
        print(f'Error: Couldn\'t find {path}')
        quit()


if __name__ == '__main__':
    # today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    main()