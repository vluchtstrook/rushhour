"""
randomise.py

Course: programmeertheorie
Team: vluchtstrook

This file contains the random algorithm. It runs on the Rushhour class and contains two functions that (1) makes random moves
and (2) generates a random winning state.
This algorithm is called from the main file (main.py).
"""


from copy import deepcopy
import random
from code.classes.grid import Grid
from code.classes.rushhour import RushHour
from code.classes.solution import Solution 
import random


def random_algo(rushhour: RushHour) -> Solution:
    """
    This function randomly moves vehicles untill a solution is found.
    """

    random_solution = Solution()

    # Add the initial state to the path.
    random_solution.path = [rushhour.grid_to_string(rushhour.grid)]

    archive = set()

    # Solve game randomly.
    while not rushhour.grid.win():
        
        # Get all moves possible in the current state.
        possible_moves = rushhour.possible_moves(rushhour.grid.grid)

        # Choose random a move.
        random_move = random.choice(possible_moves)

        # Execute the random move.
        rushhour.grid.move_in_grid(random_move[0], random_move[1], random_move[2])

        # Save all unique states.
        archive.add(rushhour.grid_to_string(rushhour.grid))

        # Add the state to the path.
        random_solution.path.append(rushhour.grid_to_string(rushhour.grid))
    
    random_solution.count_states = len(random_solution.path)
    random_solution.count_unique_states = len(archive)

    return random_solution


def random_winning_state(grid: Grid, rushhour: RushHour) -> list[list[str]]:
    """
    This function returns a random winning state after executing random moves.
    """
    grid = deepcopy(grid)

    # Solve game randomly.
    while not grid.win():
        
        # Get all moves possible in the current state.
        possible_moves = rushhour.possible_moves(grid.grid)

        # Choose random a move.
        random_move = random.choice(possible_moves)

        # Execute the random move.
        grid.move_in_grid(random_move[0], random_move[1], random_move[2])

    return grid.grid