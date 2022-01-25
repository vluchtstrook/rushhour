import math

class Grid:
    
    def __init__(self, size, new_grid):
        self.size = size
        self.grid = new_grid

    def win(self):
        # Calculate the y-coordinate of the finish
        finish = self.size // 2 if self.size % 2 == 0 else math.ceil(self.size / 2)
        
        if self.grid[finish - 1][self.size - 1] == 'X':
            return True
        return False
    
    def move_in_grid(self, vehicle_name, direction, vehicle_size):
        """
        Checks if a certain movement is possible inside the grid.
        Changes the position of a certain vehicle in a specific direction in the grid.
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == vehicle_name:

                    if direction == 'left' and j != 0 and self.grid[i][j - 1] == '_':
                        self.grid[i][j - 1] = vehicle_name
                        self.grid[i][j + vehicle_size - 1] = '_'
                        return True
                    
                    if direction == 'right' and j + vehicle_size <= self.size - 1 and self.grid[i][j + vehicle_size] == '_':
                        self.grid[i][j + vehicle_size] = vehicle_name
                        self.grid[i][j] = '_'
                        return True

                    if direction == 'up' and i != 0 and self.grid[i - 1][j] == '_':
                        self.grid[i - 1][j] = vehicle_name
                        self.grid[i + vehicle_size - 1][j] = '_'
                        return True
                    
                    if direction == 'down' and i + vehicle_size <= self.size - 1 and self.grid[i + vehicle_size][j] == "_":
                        self.grid[i + vehicle_size][j] = vehicle_name
                        self.grid[i][j] = '_'
                        return True
                        
                    return False