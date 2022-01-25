import code.loader.loader as loader

class RushHour:
    
    def __init__(self, filename):
        
        # loader.load_vehicles() returns a dictionary with all vehicle classes and a list with the keys.
        (self.vehicles, self.vehicle_names) = loader.load_vehicles(filename)

        # loader.load_grid() returns the initial grid class.
        self.grid = loader.load_grid(filename) 

        # possible moves
        self.moves = ['left', 'right', 'up', 'down']

    def display_grid(self):
        return self.grid.display_grid()

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

    def check_orientation(self, vehicle_name, direction):
        """
        Checks wheter a certain vehicle is orientationaly allow to move a certain direction.
        """
        if (direction == 'left' or direction == 'right') and self.vehicles[vehicle_name].orientation == 'H':
            return True
        elif (direction == 'up' or direction == 'down') and self.vehicles[vehicle_name].orientation == 'V':
            return True
        return False

    def move(self, vehicle_name, direction):
        """
        Checks whether the direction of the move and the vehicles orientation match.

        If so, the vehicle is tried to moved in that direction within the grid.

        Returns True or False dependent on whether it succeeded.
        """
        if self.check_orientation(vehicle_name, direction):
            return self.grid.move_in_grid(vehicle_name, direction, self.vehicles[vehicle_name].length)

    def grid_to_string(self, grid):
        """
        Converts a 2x2 list grid to a string grid.
        """
        string_grid = ''

        for i in range(self.grid.size):
            for j in range(self.grid.size):
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