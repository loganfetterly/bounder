# This file outputs Addresses within a bounding box provided from text file.
# This file uses geopy to geocode the addresses

# Installation: pip install geopy


# IMPORTS
import re
from geopy.geocoders import Nominatim

# MAIN BLOCK

class Bounder:

    # Fields:
    #     file - file object for reading
    #     allAddresses - all addresses before determining within bounding
    #     inBoxAddresses - all addresses within the bounds
    #     boundingBox - coordinates for the bounding shape
    #     geoCoder - geocoder for getting long and lat from addresses
    #     lines - an array of string (lines) from the input file

    def __init__(self, file):
        self.file = open(file)
        self.allAddresses = []
        self.inBoxAddresses = []
        self.boundingBox = []
        self.geoCoder = Nominatim(user_agent="app.py")
        self.lines = self.file.readlines()

    # If in bounds append to inBoxAddresses
    # def inBounds(self):

    # Take file and get the bounding information inside the boundingBox array
    # EXAMPLE INPUT (37.5, -122.5), (38.2, -121.6), (37.0, -121.4), (36.6, -121.3)

    def getBounds(self):
        coordinatePoints = re.findall(r"[+-]?\d+\.?\d*", self.lines[0])
        for num in range(len(coordinatePoints)):
            coordinatePoints[num] = float(coordinatePoints[num])
        self.boundingBox = coordinatePoints

    # Take all the strings of addresses and store them inside the addresses array
    def getAddresses(self):

        # GET ADDRESSES
        i = 1
        while(i < len(self.lines)):
            self.allAddresses.append(self.lines[i].replace("\n", ""))
            i += 1

# ------------------------------------------------------------
# geolocator = Nominatim(user_agent="app.py")
# location = geolocator.geocode("175 5th Avenue NYC")
# print(location.address)
# print((location.latitude, location.longitude))
# (40.7410861, -73.9896297241625)
# print(location.raw)

x = Bounder("test.txt")
x.getBounds()
x.getAddresses()