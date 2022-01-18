import vehicle


class Grid:
    
    def __init__(self, size, vehicles, vehicle_names):
        self.size = size
        self.vehicles = vehicles
        self.vehicle_names = vehicle_names
        self.grid = [['_' for i in range(self.size)] for j in range(self.size)]
        self.moves = ['left', 'right', 'up', 'down']

    def display_grid(self):
        # place vehicles in grid
        # 'vehicle' only represents the dictionary keys here
        for vehicle in self.vehicles:
            for i in range(self.vehicles[vehicle].length):
                if self.vehicles[vehicle].orientation == 'H':
                    self.grid[self.vehicles[vehicle].row][self.vehicles[vehicle].col + i] = self.vehicles[vehicle].vehicle_name
                else:
                    self.grid[self.vehicles[vehicle].row + i][self.vehicles[vehicle].col] = self.vehicles[vehicle].vehicle_name

        for i in range(self.size):
            for j in range(self.size):
                print(f'{self.grid[i][j]} ', end='')
            print('')

        # # add finish indent and return string for representation
        # if self.size % 2 == 0:
        #     finish = self.size // 2
        # else:
        #     finish = int(round(self.size / 2.0))

        # self.grid[finish - 1].insert(self.size, '<')

        # return ''.join([''.join(row) + '\n' for row in self.grid])
        
    
    def delete_position(self, vehicle_name):
    # deletes the old position of a vehicle before moving

        vehicle = self.vehicles[vehicle_name]

        for i in range(vehicle.length):
            if vehicle.orientation == 'H':
                self.grid[vehicle.row][vehicle.col + i] = '_'
            else:
                self.grid[vehicle.row + i][vehicle.col] = '_'
    
    def valid_move(self, vehicle_name, direction):
    # checks if move is possible

        # Get choosen vehicle from vehicle dictionary.
        vehicle = self.vehicles[vehicle_name]

        if direction == 'left' and vehicle.orientation == 'H' and vehicle.col != 0 and self.grid[vehicle.row][vehicle.col - 1] == '_':
            return True
        
        if direction == 'right' and vehicle.orientation == 'H' and vehicle.col + vehicle.length <= self.size - 1 and self.grid[vehicle.row][vehicle.col + vehicle.length] == '_':
            return True
        
        if direction == 'up' and vehicle.orientation == 'V' and vehicle.row != 0 and self.grid[vehicle.row - 1][vehicle.col] == '_':
            return True

        if direction == 'down' and vehicle.orientation == 'V' and vehicle.row + vehicle.length <= self.size - 1 and self.grid[vehicle.row + vehicle.length][vehicle.col] == '_':
            return True

        return False

    def move(self, vehicle_name, direction):
    # tries to move a vehicle

        vehicle = self.vehicles[vehicle_name]

        if direction == 'left':
            if self.valid_move(vehicle_name, direction):
                self.delete_position(vehicle_name)
                vehicle.col -= 1
                return True
            return False

        if direction == 'right':
            if self.valid_move(vehicle_name, direction):
                self.delete_position(vehicle_name)
                vehicle.col += 1
                return True
            return False

        if direction == 'down':
            if self.valid_move(vehicle_name, direction):
                self.delete_position(vehicle_name)
                vehicle.row += 1
                return True
            return False

        if direction == 'up':
            if self.valid_move(vehicle_name, direction):
                self.delete_position(vehicle_name)
                vehicle.row -= 1
                return True
            return False
