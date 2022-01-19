from fileinput import filename
from code.classes.rushhour import RushHour
import code.algorithms.randomise as randomise
import code.visualisation.visualisation as visualisation

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
    filename = f"data/{game_name}"

    # Create game
    rushhour = RushHour(filename)
    
    # Welcome user
    print("Welcome to Rushhour.\n")

    # Print starting positions of vehicles on grid
    rushhour.display_grid()

    # Run the random algorithm
    random_solution = randomise.random_algo(rushhour, rushhour.grid.size)

    # Print the state history
    visualisation.visualisation(random_solution, rushhour.grid.size)

