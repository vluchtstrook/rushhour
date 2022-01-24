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
        self.states = [self.grid_to_string(self.initial_grid)]
        self.archive = set()
        self.solution = Solution()
    
    def grid_to_string(self, grid):
        """
        Converts a 2x2 list grid to a string grid.
        """
        string_grid = ''

        for i in range(self.initial_grid.size):
            for j in range(self.initial_grid.size):
                string_grid += grid.grid[i][j]
        
        return string_grid
    
    def string_to_grid(self, string_grid):
        """
        Converts a string grid to a 2x2 list grid.
        """
        # 2x2 array to respresent the grid
        grid = [['_' for i in range(self.initial_grid.size)] for j in range(self.initial_grid.size)]

        # filling the grid
        for i in range(self.initial_grid.size):
            for j in range(self.initial_grid.size):
                grid[i][j] = string_grid[j + (i * self.initial_grid.size)]
        
        return grid 

    def possible_moves(self, grid):
        """
        Method that derives all the possible moves given a current state.
        """
        moves = []
        for i in range(self.initial_grid.size):
            for j in range(self.initial_grid.size):
                if grid[i][j] == '_':
                    if i - 1 > 0 and grid[i - 1][j] != '_' and self.vehicles[grid[i - 1][j]].orientation == 'V':
                        moves.append([grid[i - 1][j], 'down', self.vehicles[grid[i - 1][j]].length])

                    if i + 1 < self.size - 1 and grid[i + 1][j] != '_' and self.vehicles[grid[i + 1][j]].orientation == 'V':
                        moves.append([grid[i + 1][j], 'up', self.vehicles[grid[i + 1][j]].length])

                    if j - 1 > 0 and grid[i][j - 1] != '_' and self.vehicles[grid[i][j - 1]].orientation == 'H':
                        moves.append([grid[i][j - 1],'right', self.vehicles[grid[i][j - 1]].length])

                    if j + 1 < self.size - 1 and grid[i][j + 1] != '_' and self.vehicles[grid[i][j + 1]].orientation == 'H':
                        moves.append([grid[i][j + 1], 'left', self.vehicles[grid[i][j + 1]].length])

        return moves
                
    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)


    def run(self):
        while self.states:
            parent_grid = self.string_to_grid(self.get_next_state())

            parent_grid = Grid(self.initial_grid.size, parent_grid)

            if self.grid_to_string(parent_grid) not in self.archive:
                for move in self.possible_moves(parent_grid.grid):
                    child_grid = copy.deepcopy(parent_grid)

                    child_grid.move_in_grid(move[0], move[1], move[2])
                    
                    if child_grid.win():
                        self.solution.states.append(self.grid_to_string(child_grid))
                        self.solution.moves_made.append('This is still without memory path.')
                        return self.solution

                    if self.grid_to_string(child_grid) not in self.archive:
                        self.states.append(self.grid_to_string(child_grid))
            
            self.archive.add(self.grid_to_string(parent_grid))