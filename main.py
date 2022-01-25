from fileinput import filename
from code.algorithms.depth_first import DepthFirst
from code.classes.rushhour import RushHour
import code.algorithms.randomise as randomise
import code.algorithms.breadth_first as breadth_first
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

    # ----------------------------------------- Run the random algorithm ---------------------------------------
    # random_solution = randomise.random_algo(rushhour, rushhour.grid.size)
    # visualisation.visualisation(random_solution, rushhour.grid.size)

    # ------------------------------------- Run the breadth first algorithm ------------------------------------
    # print("This is the Breadth First algorithm:\n")
    # breadth_first_class = breadth_first.BreadthFirst(rushhour)
    # breadth_first_solution = breadth_first_class.run()
    # visualisation.visualisation(breadth_first_solution, rushhour.grid.size)  

    # ------------------------------------- Run the breadth first algorithm ------------------------------------
    print("This is the Depth First algorithm:\n")
    depth_first_class = DepthFirst(rushhour)
    depth_first_solution = depth_first_class.run()
    visualisation.visualisation(depth_first_solution, rushhour.grid.size)  

