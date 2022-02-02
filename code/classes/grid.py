"""
grid.py

Course: programmeertheorie
Team: vluchtstrook

This file contains a class named Grid. It defines two methods that (1) calculates the 'exit' of the grid and checks if 
the red car (or car 'X') of the grid is in the exit spot and (2) checks if a specific move is legal.
An instance of the Grid class is created in the loader file (loader.py).
"""


import math


class Grid:
    
    def __init__(self, size: int, new_grid: list[list[str]]) -> None:
        self.size = size
        self.grid = new_grid

    def win(self) -> bool:
        """
        This method calculates the y-coordinate of the exit and checks if the grid is a winning state.
        """

        finish = self.size // 2 if self.size % 2 == 0 else math.ceil(self.size / 2)
        
        if self.grid[finish - 1][self.size - 1] == 'X':
            return True
        return False
    

    def move_in_grid(self, vehicle_name: str, direction: str, vehicle_size: int) -> bool:
        """
        This method checks if a specific move is possible inside the grid. It changes the position of the vehicle
        in the grid in a specific direction if the move is possible.
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
