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

