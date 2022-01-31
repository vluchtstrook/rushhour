import copy
import math
import random
import heapq
import queue
from code.classes import solution, vehicle
from code.classes.grid import Grid
from code.classes.solution import Solution

class Greedy():
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
        # Beginning value for the costs
        lowest_costs = 1000
        
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

                # Dictionary with the costs per child, the child_grid as key and costs as value
                costs_childs = {}

                # Create every possible child through every possible move
                for move in self.rushhour.possible_moves(parent_grid.grid):
                    childs_grid = copy.deepcopy(parent_grid)
                    self.solution.count_states += 1

                    # Make child
                    childs_grid.move_in_grid(move[0], move[1], move[2])
                    
                    # Check whether the child is a winning state
                    if childs_grid.win():
                        self.solution.path = self.get_path(childs_grid, parent_grid, self.path_memory)
                        return self.solution

                    # Save the costs of each child
                    child_costs = self.H1_costs(childs_grid) + parent_depth

                    # Check if the previous child has lower costs and take the (first) lowest child
                    if child_costs < lowest_costs:
                        lowest_costs = child_costs
                        child_grid = childs_grid
                    
                print(child_grid)

                    # Add to a dictionary the costs per child
                    # costs_childs[child_grid] = child_costs

                # Choice based on costs:
                # Check which child has the lowest costs, choose random if more childs have the same costs 
                # and push only that child to the queue
                # child_grid = min(costs_childs, key=costs_childs.get)
                # print(child_grid)
            
                # Choose a random child from the dictionary
                # child_grid = random.choice(list(costs_childs.keys()))

                # Add that child to the queue if its state has not been in the queue before
                if self.rushhour.grid_to_string(child_grid) not in self.archive:
                    print("komt hier")

                    self.solution.count_unique_states += 1

                    heapq.heappush(self.heap, (self.H1_costs(child_grid) + parent_depth + 1, parent_depth + 1 ,self.rushhour.grid_to_string(child_grid)))

                    self.path_memory[self.rushhour.grid_to_string(child_grid)] = self.rushhour.grid_to_string(parent_grid)

                # Add the parent to the archive to rember its state has already been investigated
                self.archive.add(self.rushhour.grid_to_string(parent_grid))

                # Clean the dictionary for the next childs
                costs_childs.clear()


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



