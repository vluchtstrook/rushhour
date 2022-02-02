"""
generate_solutions.py

Course: programmeertheorie
Team: vluchtstrook

This file contains a class named GenerateSolutions. It uses the breadth first algorithm to retrieve a specific amount of 
winning states.
"""


import copy
from typing import Dict, List
from code.classes.grid import Grid
from code.classes.rushhour import RushHour
from code.classes.solution import Solution


class GenerateSolutions:
    def __init__(self, rushhour: RushHour, amount: int) -> None:
        # Import data from rushhour.
        self.amount = amount
        self.rushhour = rushhour
        self.initial_grid = rushhour.grid
        self.size = rushhour.grid.size
        self.vehicles = rushhour.vehicles

        # Algorithm specific variables.
        self.queue = [self.rushhour.grid_to_string(self.initial_grid)]
        self.archive = set()
        self.path_memory = {self.rushhour.grid_to_string(self.initial_grid): ''}
        self.solution = Solution()
        self.count_win_states = 0
        self.winning_states = []
                

    def get_next_state(self) -> str:
        """
        This method gets the next state from the queue.
        """
        return self.queue.pop(0)

    def run(self) -> List[int]:
        """
        This method runs the algorithm untill all possible states are visited. It returns a list of winning states.
        """

        while self.queue and len(self.winning_states) <= self.amount:
            
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
                    
                    # Check whether child is a winning state.
                    if child_grid.win() and self.rushhour.grid_to_string(child_grid) not in self.archive:
                        self.count_win_states += 1
                        print(self.count_win_states)
                        self.solution.path = self.get_path(child_grid, parent_grid, self.path_memory)
                        self.winning_states.append(len(self.solution.path))

                    # Add child to the queue if child is unique.
                    if self.rushhour.grid_to_string(child_grid) not in self.archive:
                        self.solution.count_unique_states += 1
                        self.queue.append(self.rushhour.grid_to_string(child_grid))
                        self.path_memory[self.rushhour.grid_to_string(child_grid)] = self.rushhour.grid_to_string(parent_grid)

                # Add parent to the archive.
                self.archive.add(self.rushhour.grid_to_string(parent_grid))
        
        return self.winning_states


    def get_path(self, child_grid: Grid, parent_grid: Grid, path_memory: Dict[str, str]) -> List[str]:
        """
        This method returns the path that led to the solution.
        """

        # Insert winning state to path
        path = [self.rushhour.grid_to_string(child_grid)]

        # Turn parent grid into a string 
        parent_grid = self.rushhour.grid_to_string(parent_grid)

        # Find all child - parent relations and add each parent to the path
        while parent_grid != '':
            path.insert(0, parent_grid)
            parent_grid = path_memory[parent_grid]
        
        return path
