#-----------------------------------------------------
# vehicle.py
#
# Programmeertheorie
# Vluchtstrook
#
# - This file is one of the parts of rushhour
# - This file defines a class named Vehicle
# - A new object of this class has specific attributes
# - It has different methods to return the object's attribute
#-----------------------------------------------------

class Vehicle():
    
    def __init__(self, car, orientation, length):
        self.car = car
        self.orientation = orientation
        self.length = length
    
    def __str__(self):
        return self.car
    
    def orientation(self):
        return self.orientation
    
    def length(self):
        return self.length

