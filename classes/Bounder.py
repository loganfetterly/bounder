# This file outputs Addresses within a bounding box provided from text file.
# This file uses geopy to geocode the addresses

# Installation: pip install geopy
# Installation: 

# IMPORTS
import re
from geopy.geocoders import Nominatim
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# MAIN BLOCK

class Bounder:

    # Fields:
    #     file - file object for reading
    #     allAddresses - all addresses before determining within bounding
    #     addressPoints - Point objects from Shapely created after geocoding 
    #     inBoxAddresses - all addresses within the bounds
    #     boundingInput - coordinates for the bounding shape
    #     boundingPoints - Point Tuples for creation of a Polygon
    #     geoCoder - geocoder for getting long and lat from addresses
    #     lines - an array of string (lines) from the input file

    def __init__(self, file):
        self.file = open(file)
        self.allAddresses = []
        self.addressPoints = []
        self.inBoxAddresses = []
        self.boundingInput = []
        self.boundingPoints = []
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
        self.boundingInput = coordinatePoints

    # Take all the strings of addresses and store them inside the addresses array
    def getAddresses(self):
        i = 1
        while(i < len(self.lines)):
            self.allAddresses.append(self.lines[i].replace("\n", ""))
            i += 1

    # Convert list of floats in boundingBox to Point Tuples for Shapely
    def convertBoundsToPoints(self):
        i = 0
        while(i < len(self.boundingInput)):
            self.boundingPoints.append((self.boundingInput[i], self.boundingInput[i + 1]))
            i += 2
    
    # Geocode addresses into Shapely Points
    def geoCode(self):
        for address in self.allAddresses:
            loc = self.geoCoder.geocode(address)
            self.addressPoints.append(Point(loc.latitude, loc.longitude))

    # Determine if Points are inside a polygon created by Point Tuples of the input
    def isAllInside(self):

        # Create a polygon
        polygon = Polygon(self.boundingPoints)

        # Use Shapely's contain method to determine if address is inside
        i = 0
        for i in range(len(self.addressPoints)):
            if (polygon.contains(self.addressPoints[i])):
                self.inBoxAddresses.append(self.allAddresses[i])

    # Calls all necessary functions in order for completion
    def printOutput(self):
        self.getBounds()
        self.getAddresses()
        self.convertBoundsToPoints()
        self.geoCode()
        self.isAllInside()
        for address in self.inBoxAddresses:
            print("Inside polygon: ", address)