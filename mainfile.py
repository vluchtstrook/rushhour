from fileinput import filename
import random
import grid
import loader


class RushHour:
    
    def __init__(self, filename):
        #loader.load_vehicles() returns a variable of type grid class.
        self.grid = loader.load_vehicles(filename)
    
    def display_grid(self):
        return self.grid.display_grid()
    
    def random_algo(self):
    # random algorithm to move around vehicles
        count = 1
        while self.grid.grid[2][5] != 'X':

            # Choose a random vehicle and store it's name. 
            # Convert vehicle set to tuple because sets are invalid inputs
            random_vehicle = random.choice(self.grid.vehicle_names)

            # Choose a random move 
            random_move = random.choice(self.grid.moves)

            if self.grid.move(random_vehicle, random_move) == True:
                print(f'\'{random_vehicle}\' moved {random_move}:')
                print('------------')
                self.display_grid()
                print()
            
            count += 1

        print(f'It took {count} random steps.', end = '\n\n')
    

if __name__ == "__main__":
    
    from sys import argv

    # Check command line arguments
    if len(argv) not in [1, 2]:
        print("Usage: python3 main.py [name]")
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
    rushhour.display_grid()

    rushhour.random_algo()