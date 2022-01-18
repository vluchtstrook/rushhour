import random

def random_algo(rushhour):
    """
    Contains the process of randomly moving around vehicles in the grid untill a solution state is found.
    Still only for 6x6 puzzles.
    """
    count = 1
    
    # Still only applicable to 6x6 puzzles
    while rushhour.grid.grid[2][5] != 'X':

        # Choose a random vehicle and store it's name
        random_vehicle = random.choice(rushhour.vehicle_names)

        # Choose a random move 
        random_direction = random.choice(rushhour.moves)

        # Print the grid each time a valid move has been made
        if rushhour.move(random_vehicle, random_direction) == True:
            print(f'\'{random_vehicle}\' moved {random_direction}:')
            print('------------')
            for i in range(len(rushhour.grid.grid)):
                for j in range(len(rushhour.grid.grid[i])):
                    print(rushhour.grid.grid[i][j], end = ' ')
                print()
            print()
        
        count += 1

    # Show the amount of steps it took to come up with a random solution
    print(f'It took {count} random steps.', end = '\n\n')