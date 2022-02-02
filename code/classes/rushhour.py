"""
rushhour.py

Course: programmeertheorie
Team: vluchtstrook

- This file contains a class named Rushhour. It defines methods that (1) derive all possible moves for 
- a given state, (2) convert a Grid instance to a string and (3) convert a string to a 2x2 list.
- An instance of the Rushhour class is created in the main file (main.py).
"""

import code.loader.loader as loader


class RushHour:
    
    def __init__(self, filename):
        
        # Store dictionary with all vehicle instances and a list of vehicle names.
        self.vehicles, self.vehicle_names = loader.load_vehicles(filename)

        # Store the initial grid.
        self.grid = loader.load_grid(filename) 
        

    def possible_moves(self, grid):
        """
        This method derives all possible moves given a current grid state and stores it in a list. The list of moves
        is returned. 
        """

        # Create list to store possible moves.
        moves = []
        for i in range(self.grid.size):
            for j in range(self.grid.size):

                # Find vacant spots in the grid.
                if grid[i][j] == '_':

                    # Check which surrounding vehicles could move to vacant spot. 
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
        This method converts a Grid instance to a string. It returns the string.
        """

        string_grid = ''

        for i in range(grid.size):
            for j in range(grid.size):
                string_grid += grid.grid[i][j]

        return string_grid
    

    def string_to_grid(self, string_grid):
        """
        This method converts a string to a 2x2 list grid. It returns the list grid.
        """
        
        # 2x2 list to respresent the grid.
        list_grid = [['_' for i in range(self.grid.size)] for j in range(self.grid.size)]

        # Filling the list.
        for i in range(self.grid.size):
            for j in range(self.grid.size):
                list_grid[i][j] = string_grid[j + (i * self.grid.size)]
        
        return list_grid 