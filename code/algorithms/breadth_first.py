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
        while self.states:
            parent_grid = self.rushhour.string_to_grid(self.get_next_state())

            parent_grid = Grid(self.initial_grid.size, parent_grid)

            if self.rushhour.grid_to_string(parent_grid) not in self.archive:
                for move in self.rushhour.possible_moves(parent_grid.grid):
                    child_grid = copy.deepcopy(parent_grid)

                    child_grid.move_in_grid(move[0], move[1], move[2])
                    
                    if child_grid.win():
                        self.solution.states.append(self.rushhour.grid_to_string(child_grid))
                        self.solution.moves_made.append('This is still without memory path.')
                        return self.solution

                    if self.rushhour.grid_to_string(child_grid) not in self.archive:
                        self.states.append(self.rushhour.grid_to_string(child_grid))
            
            self.archive.add(self.rushhour.grid_to_string(parent_grid))