import copy
import math
import heapq
import queue
from code.algorithms.randomise import random_algo, random_winning_state
from code.classes import solution, vehicle
from code.classes.grid import Grid
from code.classes.solution import Solution


class Astar():
    """
    This algorithm builds a queue of possible state of the game.
    Only unique states are in the queue (no repetitions of states)
    """

    def __init__(self, rushhour) -> None:

        # Info from rushhour
        self.rushhour = rushhour
        self.initial_grid = rushhour.grid
        self.size = rushhour.grid.size
        self.vehicles = rushhour.vehicles

        # self.average_win_grid = self.prefered_position(self.initial_grid, self.rushhour)

        # Create the priority queue
        self.heap = []
        self.initial_H1_costs = self.H1_costs(self.initial_grid)
        heapq.heappush(self.heap, (self.initial_H1_costs, 0, self.rushhour.grid_to_string(self.initial_grid)))

        # Algorithm specific variables
        self.archive = set()

        # path_memory = {'string_child' : 'string_parent'}
        self.path_memory = {self.rushhour.grid_to_string(self.initial_grid): ''}
        self.solution = Solution()
                
    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return heapq.heappop(self.heap)

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.heap:
            
            # Get the next parent state priority queue
            parent = self.get_next_state()

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
                        print(self.solution.count_unique_states)
                        print(parent_depth)

                        heapq.heappush(self.heap, (self.H1_costs(child_grid) + parent_depth + 1, parent_depth + 1 ,self.rushhour.grid_to_string(child_grid)))

                        self.path_memory[self.rushhour.grid_to_string(child_grid)] = self.rushhour.grid_to_string(parent_grid)

                # Add the parent to the archive to rember its state has already been investigated
                self.archive.add(self.rushhour.grid_to_string(parent_grid))


    def get_path(self, child_grid, parent_grid, path_memory):
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

    def vehicles_in_the_way(self, child_grid):
        """
        Counts the amount of cars that are between the red car and the exit of the bord.
        """
        finish_row_index = child_grid.size // 2 if child_grid.size % 2 == 0 else math.ceil(child_grid.size / 2)

        finish_row = child_grid.grid[finish_row_index - 1]

        X_index = 0

        for i in range(len(finish_row)):
            if finish_row[i] == 'X':
                X_index = i
                break
        
        obstacles = set(finish_row[X_index + 2:])
        obstacles.discard('_')

        return (obstacles, X_index)


    def H1_costs(self, child_grid):
        """
        Returns the total costs which is the manhattan distance + amount of cars in the way to the exit.
        """
        obstacles = self.vehicles_in_the_way(child_grid)

        return len(obstacles[0]) + child_grid.size - obstacles[1] + 2


    def H2_costs(self, child_grid):
        """
        Calculates the lower bound blocking which is H1 plus the minimum number of vehicles that block these vehicles in H2.

        """
        obstacles = self.vehicles_in_the_way(child_grid)

        finish_row_index = child_grid.size // 2 if child_grid.size % 2 == 0 else math.ceil(child_grid.size / 2)

        score = 0

        for obstacle in obstacles[0]:
            vehicle_name = obstacle
            obstacle_info = {}
            score = 0

            for i in range(child_grid.size):
                if child_grid.grid[finish_row_index - 1][i] == vehicle_name:
                    for j in range(child_grid.size):
                        if child_grid.grid[j][i] != vehicle_name and child_grid.grid[j][i] != '_':
                            score += 1
            
        return score

    def H3_costs(self, child_grid):
        """
        Calculates the lower bound blocking which is H1 plus the minimum number of vehicles that block these vehicles in H2.
        """
        obstacles = self.vehicles_in_the_way(child_grid)
        finish_row_index = child_grid.size // 2 if child_grid.size % 2 == 0 else math.ceil(child_grid.size / 2)

        first_obstacle = ''
        index_first_obstacle = 0

        for i in range(child_grid.size - obstacles[1] + 2):
            if child_grid.grid[finish_row_index - 1][i + obstacles[1]] != '_':
                first_obstacle = child_grid.grid[finish_row_index - 1][i + obstacles[1]]
                index_first_obstacle = i
                break

        score = 0

        if first_obstacle != '':
            for i in range(child_grid.size):
                if child_grid.grid[i][index_first_obstacle] != first_obstacle and child_grid.grid[i][index_first_obstacle] != '_':
                            score += 1
        return score  


    def H5_costs(self, grid, average_win_grid):
        """
        Calculate the minimum amount of steps each car has to move to reach an end position
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

    def prefered_position(self, grid, rushhour):
        random_winning_states = []
        i = 0

        while i < 10:
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
                print(average_win_grid[i][j])
                average_win_grid[i][j] = self.most_common(average_win_grid[i][j])
        
        return average_win_grid

    def most_common(self,lst):
        return max(set(lst), key=lst.count)

