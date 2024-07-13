# This is a script to get elevation data for all toxicity sites in the USGS Dust and Sediment data

# Import libraries
import requests
import urllib
import pandas as pd

# Read in data
toxins = pd.read_csv("../../data/raw/USGS_Dust_and_Sediment/SLVDust_DataRelease.csv").dropna(how='all')

# Get elevation data
# Code reference: https://gis.stackexchange.com/a/338407

# USGS Elevation Point Query Service
#url = r'https://nationalmap.gov/epqs/pqs.php?'
#new 2023:
url = r'https://epqs.nationalmap.gov/v1/json?'


def elevation_function(df, lat_column, lon_column):
    """Query service using lat, lon. add the elevation values as a new column."""
    elevations = []
    for lat, lon in zip(df[lat_column], df[lon_column]):
                
        # define rest query params
        params = {
            'output': 'json',
            'x': lon,
            'y': lat,
            'units': 'Feet'
        }
        
        # format query string and return query value
        result = requests.get((url + urllib.parse.urlencode(params)))
        #elevations.append(result.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation'])
        #new 2023:
        elevations.append(result.json()['value'])

    df['elev_feet'] = elevations

elevation_function(toxins, 'Latitude', 'Longitude')

toxins.to_csv("../../data/modified/toxins/dust_data.csv", index=False)


