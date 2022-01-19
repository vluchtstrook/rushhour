import random

def random_algo(rushhour):
    """
    Contains the process of randomly moving around vehicles in the grid untill a solution state is found.
    Still only for 6x6 puzzles.
    """
    count = 1

    # Made to store the states and moves made
    archive = []
    moves_made = []

    # Here we need a calculation for the end position of X
    
    # Still only applicable to 6x6 puzzles
    while rushhour.grid.grid[4][8] != 'X':

        # Choose a random vehicle and store it's name
        random_vehicle = random.choice(rushhour.vehicle_names)

        # Choose a random move 
        random_direction = random.choice(rushhour.moves)

        # Print the grid each time a valid move has been made
        if rushhour.move(random_vehicle, random_direction):

            # New state
            state = ''

            for i in range(len(rushhour.grid.grid)):
                for j in range(len(rushhour.grid.grid[i])):
                    state += rushhour.grid.grid[i][j]

            # Save the state and move made
            moves_made.append(f'\'{random_vehicle}\' moved {random_direction}:')
            archive.append(state)
        
        count += 1

    return [archive, moves_made, count]