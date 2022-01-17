class Grid:
    
    def __init__(self, width, height, vehicles):
        self.width = width
        self.height = height
        self.vehicles = vehicles
    
    def span_grid(self):
        # span empty grid 
        grid = [['_' for _ in range(self.height)] for _ in range(self.width)]

        # place vehicles in grid
        for vehicle in self.vehicles:
            for i in range(vehicle.length):
                if vehicle.orientation == 'H':
                    grid[vehicle.row][vehicle.col + i] = vehicle.vehicle_name
                else:
                    grid[vehicle.col][vehicle.row + i] = vehicle.vehicle_name
    
        # add finish indent and return string for representation
        if self.height % 2 == 0:
            finish = self.height / 2
        else:
            finish = int(round(self.height / 2.0))

        grid[finish - 1].insert(self.height, '<')
        
        return ''.join([''.join(row) + '\n' for row in grid])