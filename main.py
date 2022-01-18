from fileinput import filename
from code.classes.rushhour import RushHour
import code.algorithms.randomise as randomise

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

    # Print starting positions of vehicles on grid (still printing from within the class!!)
    rushhour.display_grid()

    # Run the random algorithm (still printing from within the functions!!)
    randomise.random_algo(rushhour)