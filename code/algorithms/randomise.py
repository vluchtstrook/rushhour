from copy import deepcopy
import random
from code.classes.grid import Grid
from code.classes.rushhour import RushHour
from code.classes.solution import Solution 
import random
from code.classes.solution import Solution 
import math


def random_algo(rushhour: RushHour) -> Solution:
    """
    Contains the process of randomly moving around vehicles in the grid untill a solution state is found.
    Still only for 6x6 puzzles.
    """

    random_solution = Solution()

    # Add the initial state to the path
    random_solution.path = [rushhour.grid_to_string(rushhour.grid)]

    archive = set()

    # Solve game randomly
    while not rushhour.grid.win():
        
        # Get all moves possible in the current state
        possible_moves = rushhour.possible_moves(rushhour.grid.grid)

        # Choose random a move
        random_move = random.choice(possible_moves)

        # Execute the random move
        rushhour.grid.move_in_grid(random_move[0], random_move[1], random_move[2])

        # Save all unique states
        archive.add(rushhour.grid_to_string(rushhour.grid))

        # Add the state to the path
        random_solution.path.append(rushhour.grid_to_string(rushhour.grid))
    
    random_solution.count_states = len(random_solution.path)
    random_solution.count_unique_states = len(archive)

    return random_solution

def random_winning_state(grid: Grid, rushhour: RushHour) -> list[list[str]]:
    """
    Returns a winning state after executing random moves, untill one is found.
    """
    grid = deepcopy(grid)

    # Solve game randomly
    while not grid.win():
        
        # Get all moves possible in the current state
        possible_moves = rushhour.possible_moves(grid.grid)

        # Choose random a move
        random_move = random.choice(possible_moves)

        # Execute the random move
        grid.move_in_grid(random_move[0], random_move[1], random_move[2])

    return grid.grid