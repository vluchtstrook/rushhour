import random

def random_algo(rushhour):
    # random algorithm to move around vehicles
        count = 1
        while rushhour.grid.grid[2][5] != 'X':

            # Choose a random vehicle and store it's name. 
            # Convert vehicle set to tuple because sets are invalid inputs
            random_vehicle = random.choice(rushhour.vehicle_names)

            # Choose a random move 
            random_direction = random.choice(rushhour.moves)

            if rushhour.move(random_vehicle, random_direction) == True:
                print(f'\'{random_vehicle}\' moved {random_direction}:')
                print('------------')
                for i in range(len(rushhour.grid.grid)):
                    for j in range(len(rushhour.grid.grid[i])):
                        print(rushhour.grid.grid[i][j], end = ' ')
                    print()
                print()
            
            count += 1

        print(f'It took {count} random steps.', end = '\n\n')