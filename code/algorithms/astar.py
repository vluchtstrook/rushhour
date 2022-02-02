"""
main.py

Course: programmeertheorie
Team: vluchtstrook

This file contains the A * algorithm. It runs on the Rushhour class and contains five methods that (1) retrieves the 
next state from the list of states, (2) runs the algorithm as long as the priority queue contains states, (3) returns the path with
the states leading to the solution, (4) calculates the costs of a child grid and (5) counts the vehicles that block the 
red vehicle (vehicle 'X') from the exit.
This algorithm is called from the main file (main.py).
"""


import copy
import math
import heapq
from typing import Dict, Set
from code.classes.grid import Grid
from code.classes.rushhour import RushHour
from code.classes.solution import Solution


class Astar():
    """
    This algorithm builds a queue of possible states of the game. Only unique states are in the queue.
    """
    def __init__(self, rushhour: RushHour) -> None:

        # Import informatin from rushhour.
        self.rushhour = rushhour
        self.initial_grid = rushhour.grid
        self.size = rushhour.grid.size
        self.vehicles = rushhour.vehicles

        # Create the priority queue.
        self.heap = []
        self.initial_H1_costs = self.H1_costs(self.initial_grid)
        heapq.heappush(self.heap, (self.initial_H1_costs, 0, self.rushhour.grid_to_string(self.initial_grid)))

        # Algorithm specific variables.
        self.archive = set()
        self.path_memory = {self.rushhour.grid_to_string(self.initial_grid): ''}
        self.solution = Solution()


    def get_next_state(self) -> Set[int, int, str]:
        """
        This method gets the next state from the priority queue and returns it.
        """
        return heapq.heappop(self.heap)


    def run(self) -> Solution:
        """
        This method runs the algorithm untill all possible states are visited.
        """
        while self.heap:
            
            # Get the next parent state priority queue.
            parent = self.get_next_state()

            parent_depth = parent[1]
            parent_grid = parent[2]

            # Check whether this is a unique parent.
            if parent_grid not in self.archive:

                # Turn the parent state from string-type into 2x2 list-type.
                parent_grid = self.rushhour.string_to_grid(parent_grid)

                # Create an instance of Grid class.
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

                        heapq.heappush(self.heap, (self.H1_costs(child_grid) + parent_depth + 1, 
                                                    parent_depth + 1,
                                                    self.rushhour.grid_to_string(child_grid)))

                        # Store the parent child connection.
                        self.path_memory[self.rushhour.grid_to_string(child_grid)] = self.rushhour.grid_to_string(parent_grid)

                # Add the parent to the archive to avoid repetitive investigation.
                self.archive.add(self.rushhour.grid_to_string(parent_grid))


    def get_path(self, child_grid: Grid, parent_grid: Grid, path_memory: Dict[str, str]) -> list[str]:
        """
        This method returns the path that led to the solution.
        """
        # Beginning with inserting the winning state found
        path = [self.rushhour.grid_to_string(child_grid)]

        # Turn parent grid into a string 
        parent_grid = self.rushhour.grid_to_string(parent_grid)

        # Find all child - parent relations and add each parent to the path
        while parent_grid != '':
            path.insert(0, parent_grid)
            parent_grid = path_memory[parent_grid]
        
        return path


    def H1_costs(self, child_grid: Grid) -> int:
        """
        This method returns the total costs (manhattan distance + amount of cars blocking the exit).
        """
        obstacles = self.vehicles_in_the_way(child_grid)

        return len(obstacles[0]) + child_grid.size - obstacles[1] + 2


    def vehicles_in_the_way(self, child_grid: Grid) -> set[set[str], int]:
        """
        This method counts the amount of cars that are blocking the red car (car 'X') from the exit.
        """
        finish_row_index = child_grid.size // 2 if child_grid.size % 2 == 0 else math.ceil(child_grid.size / 2)
        finish_row = child_grid.grid[finish_row_index - 1]

        # Find and store the position of the red car.
        X_index = 0
        for i in range(len(finish_row)):
            if finish_row[i] == 'X':
                X_index = i
                break
        
        # All obstacles remaining between the red car and the exit.
        obstacles = set(finish_row[X_index + 2:])
        obstacles.discard('_')

        return (obstacles, X_index)