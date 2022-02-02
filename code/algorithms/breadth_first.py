"""
breadth_first.py

Course: programmeertheorie
Team: vluchtstrook

This file contains the breadth first algorithm. It runs on the Rushhour class and contains three methods that (1) retrieves the 
next state from the list of states, (2) runs the algorithm as long as the queue contains states, (3) returns the path with
the states leading to the solution.
This algorithm is called from the main file (main.py).
"""


import copy
from typing import Dict
from code.classes.grid import Grid
from code.classes.solution import Solution

class BreadthFirst():
    """
    This algorithm creates a queue of possible states of the game. Only unique states are in the queue.
    """
    def __init__(self, rushhour) -> None:
        # Import data from rushhour.
        self.rushhour = rushhour
        self.initial_grid = rushhour.grid
        self.size = rushhour.grid.size
        self.vehicles = rushhour.vehicles

        # Algorithm specific variables.
        self.queue = [self.rushhour.grid_to_string(self.initial_grid)]
        self.archive = set()

        # Create dictionary to link child state to parent state.
        self.path_memory = {self.rushhour.grid_to_string(self.initial_grid): ''}
        self.solution = Solution()


    def get_next_state(self) -> str:
        """
        This method gets the next state from the queue.
        """
        return self.queue.pop(0)


    def run(self) -> Solution:
        """
        This method runs the algorithm untill all possible states are visited.
        """

        while self.queue:
            
            # Get the next parent state from the grid.
            parent_grid = self.get_next_state()

            # Check whether state is unique parent.
            if parent_grid not in self.archive:

                # Turn parent state from string-type into 2x2 list-type.
                parent_grid = self.rushhour.string_to_grid(parent_grid)

                # Create an instance of the Grid class.
                parent_grid = Grid(self.initial_grid.size, parent_grid)

                # Create every possible child through every possible move.
                for move in self.rushhour.possible_moves(parent_grid.grid):
                    child_grid = copy.deepcopy(parent_grid)
                    self.solution.count_states += 1

                    # Make child.
                    child_grid.move_in_grid(move[0], move[1], move[2])
                    
                    # Check if child is a winning state.
                    if child_grid.win():
                        self.solution.path = self.get_path(child_grid, parent_grid, self.path_memory)
                        return self.solution

                    # If child is unique, add to queue.
                    if self.rushhour.grid_to_string(child_grid) not in self.archive:
                        self.solution.count_unique_states += 1
                        self.queue.append(self.rushhour.grid_to_string(child_grid))
                        self.path_memory[self.rushhour.grid_to_string(child_grid)] = self.rushhour.grid_to_string(parent_grid)

                # Add parent to archive.
                self.archive.add(self.rushhour.grid_to_string(parent_grid))


    def get_path(self, child_grid: Grid, parent_grid: Grid, path_memory: Dict[str, str]) -> list[str]:
        """
        This method returns the path that led to the solution.
        """

        # Inserting the winning state.
        path = [self.rushhour.grid_to_string(child_grid)]

        # Turn parent grid into a string.
        parent_grid = self.rushhour.grid_to_string(parent_grid)

        # Find all child - parent relations and add each parent to the path.
        while parent_grid != '':
            path.insert(0, parent_grid)
            parent_grid = path_memory[parent_grid]
        
        return path