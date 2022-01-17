class Grid:
    
    def __init__(self, size, vehicles):
        self.size = size
        self.vehicles = vehicles
        self.grid = [['_' for _ in range(self.size)] for _ in range(self.size)]
        self.moves = ['left', 'right', 'up', 'down']

    def span_grid(self):
        # place vehicles in grid
        for vehicle in self.vehicles:
            for i in range(vehicle.length):
                if vehicle.orientation == 'H':
                    self.grid[vehicle.row][vehicle.col + i] = vehicle.vehicle_name
                else:
                    self.grid[vehicle.row + i][vehicle.col] = vehicle.vehicle_name
    
        # add finish indent and return string for representation
        if self.size % 2 == 0:
            finish = self.size // 2
        else:
            finish = int(round(self.size / 2.0))

        self.grid[finish - 1].insert(self.size, '<')
        
        return ''.join([''.join(row) + '\n' for row in self.grid])
    
    def delete_position(self, vehicle):
    # deletes the old position of a vehicle after moving

        for i in range(vehicle.length):
            if vehicle.orientation == 'H':
                self.grid[vehicle.row][vehicle.col + i] = '_'
            else:
                self.grid[vehicle.col][vehicle.row + i] = '_'
    
    def valid_move(self, vehicle, direction):
    # checks if move is possible
        if direction == 'left' and vehicle.orientation == 'H' and vehicle.col != 0 and self.grid[vehicle.row][vehicle.col - 1] == '_':
            return True
        
        if direction == 'right' and vehicle.orientation == 'H' and vehicle.col + vehicle.length <= self.size - 1 and self.grid[vehicle.row][vehicle.col + vehicle.length] == '_':
            return True
        
        if direction == 'up' and vehicle.orientation == 'V' and vehicle.row != 0 and self.grid[vehicle.row - 1][vehicle.col] == '_':
            return True

        if direction == 'down' and vehicle.orientation == 'V' and vehicle.row + vehicle.length <= self.size - 1 and self.grid[vehicle.row + vehicle.length][vehicle.col] == '_':
            return True

        return False

    def move(self, vehicle, direction):
    # tries to move a vehicle

        if direction == 'left':
            if self.valid_move(vehicle, direction):
                self.delete_position(vehicle)
                vehicle.col -= 1
                return True
            return False

        if direction == 'right':
            if self.valid_move(vehicle, direction):
                self.delete_position(vehicle)
                vehicle.col += 1
                return True
            return False

        if direction == 'down':
            if self.valid_move(vehicle, direction):
                self.delete_position(vehicle)
                vehicle.row += 1
                return True
            return False

        if direction == 'up':
            if self.valid_move(vehicle, direction):
                self.delete_position(vehicle)
                vehicle.row -= 1
                return True
            return False
