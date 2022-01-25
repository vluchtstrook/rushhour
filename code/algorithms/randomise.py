import random
from code.classes.solution import Solution 
import math

def random_algo(rushhour, size):
    """
    Contains the process of randomly moving around vehicles in the grid untill a solution state is found.
    Still only for 6x6 puzzles.
    """

    random_solution = Solution()

    # Calculate the y-coordinate of the finish
    finish = size // 2 if size % 2 == 0 else math.ceil(size / 2)

    # Solve game randomly
    while rushhour.grid.grid[finish - 1][size - 1] != 'X':

        # Choose a random vehicle and store it's name
        random_vehicle = random.choice(rushhour.vehicle_names)

        # Choose a random move 
        random_direction = random.choice(rushhour.moves)

        # Print the grid each time a valid move has been made
        if rushhour.move(random_vehicle, random_direction):

            # Create empty state
            state = ''

            for i in range(len(rushhour.grid.grid)):
                for j in range(len(rushhour.grid.grid[i])):
                    state += rushhour.grid.grid[i][j]

            # Save the state and move made
            random_solution.moves_made.append(f'\'{random_vehicle}\' moved {random_direction}:')
            random_solution.states.append(state)
        
        random_solution.count += 1

    return random_solution