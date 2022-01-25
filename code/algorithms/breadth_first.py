import copy
from code.classes import solution
from code.classes.grid import Grid
from code.classes.solution import Solution

class BreadthFirst():
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

        # Algorithm specific variables
        self.queue = [self.rushhour.grid_to_string(self.initial_grid)]
        self.archive = set()

        # path_memory = {'string_child' : 'string_parent'}
        self.path_memory = {self.rushhour.grid_to_string(self.initial_grid): ''}
        self.solution = Solution()
                
    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.queue.pop(0)

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.queue:
            
            # Get the next parent state from the grid
            parent_grid = self.get_next_state()

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
                        self.queue.append(self.rushhour.grid_to_string(child_grid))
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

