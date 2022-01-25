import code.loader.loader as loader

class RushHour:
    
    def __init__(self, filename):
        
        # loader.load_vehicles() returns a dictionary with all vehicle classes and a list with the keys.
        (self.vehicles, self.vehicle_names) = loader.load_vehicles(filename)

        # loader.load_grid() returns the initial grid class.
        self.grid = loader.load_grid(filename) 
        

    def possible_moves(self, grid):
        """
        Method that derives all the possible moves given a current grid state.
        """
        # Iterable variable to store all the moves
        moves = []
        for i in range(self.grid.size):
            for j in range(self.grid.size):

                # Find the empty spots in the grid
                if grid[i][j] == '_':

                    # Check which surrounding vehicles could move to the empty spot. 
                    if i - 1 > 0 and grid[i - 1][j] != '_' and self.vehicles[grid[i - 1][j]].orientation == 'V':
                        moves.append([grid[i - 1][j], 'down', self.vehicles[grid[i - 1][j]].length])

                    if i + 1 < self.grid.size - 1 and grid[i + 1][j] != '_' and self.vehicles[grid[i + 1][j]].orientation == 'V':
                        moves.append([grid[i + 1][j], 'up', self.vehicles[grid[i + 1][j]].length])

                    if j - 1 > 0 and grid[i][j - 1] != '_' and self.vehicles[grid[i][j - 1]].orientation == 'H':
                        moves.append([grid[i][j - 1],'right', self.vehicles[grid[i][j - 1]].length])

                    if j + 1 < self.grid.size - 1 and grid[i][j + 1] != '_' and self.vehicles[grid[i][j + 1]].orientation == 'H':
                        moves.append([grid[i][j + 1], 'left', self.vehicles[grid[i][j + 1]].length])

        return moves


    @staticmethod
    def grid_to_string(grid):
        """
        Converts a grid class to a string grid.
        """
        string_grid = ''

        for i in range(grid.size):
            for j in range(grid.size):
                string_grid += grid.grid[i][j]

        return string_grid
    

    def string_to_grid(self, string_grid):
        """
        Converts a string grid to a 2x2 list grid.
        """
        # 2x2 list to respresent the grid
        list_grid = [['_' for i in range(self.grid.size)] for j in range(self.grid.size)]

        # filling the grid
        for i in range(self.grid.size):
            for j in range(self.grid.size):
                list_grid[i][j] = string_grid[j + (i * self.grid.size)]
        
        return list_grid 