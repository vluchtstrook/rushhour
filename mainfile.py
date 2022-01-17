from fileinput import filename
import random
import loader


class RushHour:
    
    def __init__(self, filename):
        self.grid = loader.load_vehicles(filename)
    
    def display_grid_start(self):
        return self.grid.span_grid()
    
    def display_grid(self):
        return self.grid.display_grid()

    def move(self, vehicle, direction):
        self.grid.move(vehicle, direction)
    
    # def random_algo(self):
    # # random algorithm to move around vehicles
    #     count = 1
    #     while self.filled_grid[2][5] != 'X':
    #         random_vehicle = random.choice(vehicle_types)
    #         random_move = random.choice(move_types)

    #         if move(random_vehicle, random_move) == True:
    #             print(f'{random_vehicle} moved to {random_move}')
    #             display_grid()

    #         else:
    #             print()
    #             print('Not a valid move')

    #         count += 1
    #     print(f'It took {count} random steps.')
    

# Contains all possible moves.
move_types = ['left', 'right', 'up', 'down']

# def random_algo():
#     """
#     Randomly try to move vehicles around untill a solution state has been found.
#     """
#     count = 1
#     while grid[2][5] != 'X':
#         random_vehicle = random.choice(vehicle_types)
#         random_move = random.choice(move_types)

#         if move(random_vehicle, random_move) == True:
#             print(f'{random_vehicle} moved to {random_move}')
#             display_grid()

#         else:
#             print()
#             print('Not a valid move')

#         count += 1
#     print(f'It took {count} random steps.')


if __name__ == "__main__":
    
    from sys import argv

    # Check command line arguments
    if len(argv) not in [1, 2]:
        print("Usage: python3 mainfile.py [name]")
        exit(1)

    # Load the requested game or else the first csv file
    if len(argv) == 2:
        game_name = argv[1]
    elif len(argv) == 1:
        game_name = "Rushhour6x6_1.csv"
    filename = f"gameboards/{game_name}"

    # Create game
    rushhour = RushHour(filename)
    
    # Welcome user
    print("Welcome to Rushhour.\n")

    # Print starting positions of vehicles on grid
    print(rushhour.display_grid_start())

    # Prompt the user for commands until they type QUIT
    while True:

        # prompt, converting all input to upper case
        command = input("> ").upper()
        print()
        split_command = command.split(" ")
        vehicle = split_command[0]
        direction = split_command[1]
    
        # if rushhour.move(vehicle, direction):
        #     print(rushhour.display_grid())
        # else:
        #     print('Invalid move! Try again')
        #     print(rushhour.display_grid())

        rushhour.move(vehicle, direction)
        print(rushhour.display_grid())

        if command == 'QUIT':
            break