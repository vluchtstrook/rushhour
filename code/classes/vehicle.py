"""
vehicle.py

Course: programmeertheorie
Team: vluchtstrook

This file contains a class named Vehicle. It defines two methods that (1) return the orientation of the vehicle and (2) return
the lenght of the vehicle.
An instance of the Vehicle class is created in the loader file (loader.py).
"""


class Vehicle():
    
    def __init__(self, car, orientation, length):
        self.car = car
        self.orientation = orientation
        self.length = length
    
    def __str__(self):
        return self.car
    
    def orientation(self):
        """
        This method returns the orientation of the vehicle. This can be either horizontal or vertical.
        """
        return self.orientation
    
    def length(self):
        """
        This method returns the length of the vehicle. This can be either 2 (car) or 3 (truck).
        """
        return self.length
