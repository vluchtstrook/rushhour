import copy
from code.classes.grid import Grid
from code.classes.solution import Solution

class BreadthFirst():
    """
    This algorithm builds a queue of possible state of the game.

    Only unique states are in the queue (no repetitions of states)
    """

    def __init__(self, rushhour) -> None:
        self.rushhour = rushhour
        self.initial_grid = rushhour.grid
        self.size = rushhour.grid.size
        self.vehicles = rushhour.vehicles
        self.states = [self.rushhour.grid_to_string(self.initial_grid)]
        self.archive = set()
        self.solution = Solution()
                
    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.states:
            
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

                    # Make child
                    child_grid.move_in_grid(move[0], move[1], move[2])
                    
                    # Check whether child is a winning state
                    if child_grid.win():
                        self.solution.states.append(self.rushhour.grid_to_string(child_grid))
                        self.solution.moves_made.append('This is still without memory path.')
                        return self.solution
                    
                    # Add child to the queue if its state has not been in the queue before
                    if self.rushhour.grid_to_string(child_grid) not in self.archive:
                        self.states.append(self.rushhour.grid_to_string(child_grid))

                # Add the parent to the archive to rember its state has already been investigated
                self.archive.add(self.rushhour.grid_to_string(parent_grid))