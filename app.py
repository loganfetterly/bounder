# This file outputs Addresses within a bounding box provided from text file.
# This file uses geopy to geocode the addresses

# Installation: pip install geopy


# IMPORTS
from geopy.geocoders import Nominatim

# MAIN BLOCK

geolocator = Nominatim(user_agent="app.py")
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print((location.latitude, location.longitude))
(40.7410861, -73.9896297241625)
print(location.raw)