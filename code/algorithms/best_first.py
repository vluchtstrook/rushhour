"""
best_first.py

Course: programmeertheorie
Team: vluchtstrook

This file contains the best first algorithm. It runs on the Rushhour class and contains five methods that (1) retrieves the 
next state from the list of states, (2) runs the algorithm as long as the priority queue contains states, (3) returns the path with
the states leading to the solution, (4) counts the vehicles that block the red vehicle (vehicle 'X') from the exit, (5, 6, 7) calculates 
the costs of a child grid, (8) returns the preferred position of each vehicle on the grid and (9) returns the most common
winning grid.
This algorithm is called from the main file (main.py).
"""


from typing import Dict
from code.algorithms.randomise import random_winning_state
import copy
import math
import heapq
from code.algorithms.randomise import random_winning_state
from code.classes.grid import Grid
from code.classes.rushhour import RushHour
from code.classes.solution import Solution


class BestFirst():
    """
    This algorithm builds a priority queue of possible states of the game. Priority is given based on heuristic 1 and 4 (the path lenght is not taken 
    into consideration). Only unique states are in the queue. The algorithm stops when a winning state is found, or the queue is empty.
    """
    def __init__(self, rushhour: RushHour) -> None:
        # Import data from rushhour.
        self.rushhour = rushhour
        self.initial_grid = rushhour.grid
        self.size = rushhour.grid.size
        self.vehicles = rushhour.vehicles
        self.vehicles_names = rushhour.vehicle_names

        # The amount of random winning grids to generate.
        self.repetition = 10
        self.average_win_grid = self.prefered_position(self.initial_grid, self.rushhour, self.repetition)

        # Create the priority queue.
        self.heap = []
        self.initial_H1_costs = self.H1_costs(self.initial_grid)
        heapq.heappush(self.heap, (self.initial_H1_costs, 0, self.rushhour.grid_to_string(self.initial_grid)))

        # Algorithm specific variables.
        self.archive = set()
        self.path_memory = {self.rushhour.grid_to_string(self.initial_grid): ''}
        self.solution = Solution()
                

    def get_next_state(self) -> set[int, int, str]:
        """
        This method gets the next state from the priority queue.
        """
        return heapq.heappop(self.heap)


    def run(self) -> Solution:
        """
        This method runs the algorithm untill all possible states are visited.
        """
        while self.heap:
            
            # Get the next parent state from the priority queue.
            parent = self.get_next_state()

            # Heuristic 1 and 4.
            parent_costs = parent[0]

            parent_depth = parent[1]
            parent_grid = parent[2]

            # Check whether state is a unique parent.
            if parent_grid not in self.archive:

                # Turn the parent state from string-type into 2x2 list-type.
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
                    if child_grid.win():
                        self.solution.path = self.get_path(child_grid, parent_grid, self.path_memory)
                        return self.solution
                    
                    # If child is unique, add to queue.
                    if self.rushhour.grid_to_string(child_grid) not in self.archive:

                        self.solution.count_unique_states += 1

                        heapq.heappush(self.heap, (
                            self.H1_costs(child_grid) + self.H4_costs(child_grid, self.average_win_grid), 
                            parent_depth + 1,
                            self.rushhour.grid_to_string(child_grid))
                            )

                        self.path_memory[self.rushhour.grid_to_string(child_grid)] = self.rushhour.grid_to_string(parent_grid)

                # Add parent to archive.
                self.archive.add(self.rushhour.grid_to_string(parent_grid))


    def get_path(self, child_grid: Grid, parent_grid: Grid, path_memory: Dict[str, str]) -> list[str]:
        """
        This method returns the path that led to the solution.
        """

        # Inserting the winning state.
        path = [self.rushhour.grid_to_string(child_grid)]

        # Turn parent grid into a string ,
        parent_grid = self.rushhour.grid_to_string(parent_grid)

        # Find all child - parent relations and add each parent to the path.
        while parent_grid != '':
            path.insert(0, parent_grid)
            parent_grid = path_memory[parent_grid]
        
        return path


    def vehicles_in_the_way(self, child_grid: Grid) -> set[set[str], int]:
        """
        This method counts the amount of cars that are blocking the red car (car 'X') from the exit.
        """
        finish_row_index = child_grid.size // 2 if child_grid.size % 2 == 0 else math.ceil(child_grid.size / 2)

        # Extract the row of the red car from grid.
        finish_row = child_grid.grid[finish_row_index - 1]

        # Determine the coordinates of the red car.
        X_index = 0
        for i in range(len(finish_row)):
            if finish_row[i] == 'X':
                X_index = i
                break
        
        # Collect all vehicles between the red car and finish.
        obstacles = set(finish_row[X_index + 2:])
        obstacles.discard('_')

        return (obstacles, X_index)


    def H1_costs(self, child_grid: Grid) -> int:
        """
        This method returns the total costs (manhattan distance + amount of cars blocking the exit).
        """
        obstacles = self.vehicles_in_the_way(child_grid)

        return len(obstacles[0]) + child_grid.size - obstacles[1] + 2


    def H4_costs(self, grid: Grid, average_win_grid: list[list[str]]) -> int:
        """
        This method counts the amount of mismatches of a grid compared to the average winning grid and returns the score.
        """
        score = 0
        for i in range(len(grid.grid)):
            for j in range(len(grid.grid)):
                if grid.grid[i][j] != average_win_grid[i][j]:
                    score += 1
        return score


    def H5_costs(self, grid: Grid, average_win_grid: list[list[str]]) -> int:
        """
        This method calculates the minimum amount of steps each car has to move to reach the preferred end position as determined by the average_win_grid.
        """
        score = 0

        # Store the coordinates of the vehicles of the win grid and current grid.
        win_grid_coordinates = {}
        grid_coordinates = {}

        for vehicle in self.vehicles_names:
            for i in range(len(average_win_grid)):
                for j in range(len(average_win_grid)):

                    # Store the coordinate of the first instance of the vehicles.
                    if grid.grid[i][j] == vehicle and vehicle not in grid_coordinates:
                        grid_coordinates[vehicle] = (i,j)
                    if average_win_grid[i][j] == vehicle and vehicle not in win_grid_coordinates:
                        win_grid_coordinates[vehicle] = (i,j)
        
        # Calculate the distance between the current position and prefered end position for each vehicle.
        for vehicle in self.vehicles_names:
            if self.vehicles[vehicle].orientation == 'H' and vehicle in win_grid_coordinates:
                score += abs(win_grid_coordinates[vehicle][0] - grid_coordinates[vehicle][0])
            if self.vehicles[vehicle].orientation == 'V' and vehicle in win_grid_coordinates:
                score += abs(win_grid_coordinates[vehicle][1] - grid_coordinates[vehicle][1])

        return score
       
        
    def prefered_position(self, grid: Grid, rushhour: RushHour, repetition: int) -> list[list[str]]:
        """
        This method determines the preferred (or average) state of a winning grid based on the amount of random winning states generated. It returns the
        preferred (or average) state.
        """
        random_winning_states = []
        i = 0

        # Generate random winning states a given number of times.
        while i < repetition:
            random_win = random_winning_state(grid, rushhour)
            random_winning_states.append(random_win)
            i += 1
        
        average_win_grid = [[[] for _ in range(rushhour.grid.size)] for _ in range(rushhour.grid.size)]
        
        for i in range(len(random_winning_states)):

            for j in range(len(random_winning_states[i])):
                for k in range(len(random_winning_states[i][j])):
                    average_win_grid[j][k].append(random_winning_states[i][j][k])

        for i in range(len(average_win_grid)):
            for j in range(len(average_win_grid[i])):
                average_win_grid[i][j] = self.most_common(average_win_grid[i][j])
        
        return average_win_grid


    def most_common(self, lst: list[str]) -> int:
        """
        This function returns the most common winning grid.
        """
        return max(set(lst), key=lst.count)
