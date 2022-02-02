from statistics import mode
from typing import Dict
from code.algorithms.randomise import random_winning_state
import copy
import math
import heapq
from code.algorithms.randomise import random_algo, random_winning_state
from code.classes import solution, vehicle
from code.classes.grid import Grid
from code.classes.rushhour import RushHour
from code.classes.solution import Solution


class BestFirst():
    """
    This algorithm builds a priority queue of possible states of the game.

    Priority is given based on heuristic 1 and 4. (Does not take the path lenghth into consideration)

    Only unique states are in the queue (no repetitions of states).
    
    Stops when a winning state is found, or the queue is empty.
    """

    def __init__(self, rushhour: RushHour) -> None:
        # Data from rushhour
        self.rushhour = rushhour
        self.initial_grid = rushhour.grid
        self.size = rushhour.grid.size
        self.vehicles = rushhour.vehicles
        self.vehicles_names = rushhour.vehicle_names

        # The amount of random winning grids to generate
        self.repetition = 10
        self.average_win_grid = self.prefered_position(self.initial_grid, self.rushhour, self.repetition)

        # Create the priority queue
        self.heap = []
        self.initial_H1_costs = self.H1_costs(self.initial_grid)
        heapq.heappush(self.heap, (self.initial_H1_costs, 0, self.rushhour.grid_to_string(self.initial_grid)))

        # Algorithm specific variables
        self.archive = set()
        self.path_memory = {self.rushhour.grid_to_string(self.initial_grid): ''}
        self.solution = Solution()
                
    def get_next_state(self) -> set[int, int, str]:
        """
        Method that gets the next state from the priority queue.
        """
        return heapq.heappop(self.heap)

    def run(self) -> Solution:
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.heap:
            
            # Get the next parent state priority queue
            parent = self.get_next_state()

            # H1 + H4
            parent_costs = parent[0]

            parent_depth = parent[1]
            parent_grid = parent[2]

            # Check whether we did not had this state as a parent before
            if parent_grid not in self.archive:

                # Turn the parent state from string-type into 2x2 list-type
                parent_grid = self.rushhour.string_to_grid(parent_grid)

                # Turn the parent state into a Grid class
                parent_grid = Grid(self.initial_grid.size, parent_grid)

                # Create every possible child through every possible move
                for move in self.rushhour.possible_moves(parent_grid.grid):
                    child_grid = copy.deepcopy(parent_grid)
                    self.solution.count_states += 1

                    # Make child
                    child_grid.move_in_grid(move[0], move[1], move[2])
                    
                    # Check whether child is a winning state
                    if child_grid.win():
                        self.solution.path = self.get_path(child_grid, parent_grid, self.path_memory)
                        return self.solution
                    
                    # Add child to the queue if its state has not been in the queue before
                    if self.rushhour.grid_to_string(child_grid) not in self.archive:

                        self.solution.count_unique_states += 1

                        heapq.heappush(self.heap, (
                            self.H1_costs(child_grid) + self.H4_costs(child_grid, self.average_win_grid), 
                            parent_depth + 1,
                            self.rushhour.grid_to_string(child_grid))
                            )

                        self.path_memory[self.rushhour.grid_to_string(child_grid)] = self.rushhour.grid_to_string(parent_grid)

                # Add the parent to the archive to rember its state has already been investigated
                self.archive.add(self.rushhour.grid_to_string(parent_grid))


    def get_path(self, child_grid: Grid, parent_grid: Grid, path_memory: Dict[str, str]) -> list[str]:
        """
        Returns the path that led to the solution state.
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

    def vehicles_in_the_way(self, child_grid: Grid) -> set[set[str], int]:
        """
        Counts the amount of cars that are between the red car and the exist of the bord.
        """
        finish_row_index = child_grid.size // 2 if child_grid.size % 2 == 0 else math.ceil(child_grid.size / 2)

        # Extract the row of the red car from grid
        finish_row = child_grid.grid[finish_row_index - 1]

        # Determine the coordinates of the red car
        X_index = 0
        for i in range(len(finish_row)):
            if finish_row[i] == 'X':
                X_index = i
                break
        
        # Collect all vehicles between the red car and finish
        obstacles = set(finish_row[X_index + 2:])
        obstacles.discard('_')

        return (obstacles, X_index)


    def H1_costs(self, child_grid: Grid) -> int:
        """
        Returns the total costs of manhattan distance + a, mount of cars in the way to the exit.
        """
        obstacles = self.vehicles_in_the_way(child_grid)

        return len(obstacles[0]) + child_grid.size - obstacles[1] + 2


    def H4_costs(self, grid: Grid, average_win_grid: list[list[str]]) -> int:
        """
        Counts the amount of missmatches of a grid with the average winningg grid.
        """
        score = 0
        for i in range(len(grid.grid)):
            for j in range(len(grid.grid)):
                if grid.grid[i][j] != average_win_grid[i][j]:
                    score += 1
        return score


    def H5_costs(self, grid: Grid, average_win_grid: list[list[str]]) -> int:
        """
        Calculates the minimum amount of steps each car has to move to reach the preferred end 
        position as determined by the average_win_grid
        """
        score = 0
        win_grid_coordinates = {}
        grid_coordinates = {}
        for vehicle in self.vehicles_names:
            for i in range(len(average_win_grid)):
                for j in range(len(average_win_grid)):
                    if grid.grid[i][j] == vehicle and vehicle not in grid_coordinates:
                        grid_coordinates[vehicle] = (i,j)
                    if average_win_grid[i][j] == vehicle and vehicle not in win_grid_coordinates:
                        win_grid_coordinates[vehicle] = (i,j)
        
        for vehicle in self.vehicles_names:
            if self.vehicles[vehicle].orientation == 'H' and vehicle in win_grid_coordinates:
                score += abs(win_grid_coordinates[vehicle][0] - grid_coordinates[vehicle][0])
            if self.vehicles[vehicle].orientation == 'V' and vehicle in win_grid_coordinates:
                score += abs(win_grid_coordinates[vehicle][1] - grid_coordinates[vehicle][1])

        return score
       
        
    def prefered_position(self, grid: Grid, rushhour: RushHour, repetition: int) -> list[list[str]]:
        random_winning_states = []
        i = 0

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
        return max(set(lst), key=lst.count)


