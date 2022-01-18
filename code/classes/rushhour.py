import code.loader as loader


class RushHour:
    
    def __init__(self, filename):
        # loader.load_vehicles() returns a dictionary with all vehicle classes and a list with the keys.
        (self.vehicles, self.vehicle_names) = loader.load_vehicles(filename)

        # loader.load_grid() returns the grid class.
        self.grid = loader.load_grid(filename) 

        # possible moves
        self.moves = ['left', 'right', 'up', 'down']

    def display_grid(self):
        return self.grid.display_grid()

    def move(self, vehicle_name, direction):
        if (direction == 'left' or direction == 'right') and self.vehicles[vehicle_name].orientation == 'H':
            return self.grid.move_in_grid(vehicle_name, direction, self.vehicles[vehicle_name].length)

        elif (direction == 'up' or direction == 'down') and self.vehicles[vehicle_name].orientation == 'V':
            return self.grid.move_in_grid(vehicle_name, direction, self.vehicles[vehicle_name].length)
