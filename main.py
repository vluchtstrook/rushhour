from fileinput import filename
import code.algorithms.randomise as randomise
from code.algorithms.astar import Astar
from code.algorithms.greedy import Greedy
from code.algorithms.depth_first import DepthFirst
from code.algorithms.breadth_first import BreadthFirst
from code.algorithms.best_first import BestFirst
from code.classes.rushhour import RushHour
import code.visualisation.visualisation as visualisation
import code.visualisation.pygamegui as pygamegui
import code.visualisation.output_to_csv as output_to_csv
import time


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
    # random_solution = randomise.random_algo(rushhour)
    # visualisation.visualisation(random_solution, rushhour.grid.size)
    # pygamegui.visualize(random_solution, rushhour.grid.size)
    # print(f"This was the Random algorithm on {game_name[:-4]}.\n") 
    # output_to_csv.output(rushhour.grid.size, random_solution.path, game_name, algorithm='Random')


    # ------------------------------------- Run the breadth first algorithm ------------------------------------
    start = time.time()
    breadth_first_class = BreadthFirst(rushhour)
    breadth_first_solution = breadth_first_class.run()

    # # print(f'Amount of unique winning states: {breadth_first_solution[0]}', end = '\n\n')
    # # print()
    # # print(f'Amount of states: {breadth_first_solution[1]}', end = '\n\n')
    # # print()
    # # print(f'Amount of unique states: {breadth_first_solution[2]}', end = '\n\n')
    # # print()

    end = time.time()
    visualisation.visualisation(breadth_first_solution, rushhour.grid.size)
    pygamegui.visualize(breadth_first_solution, rushhour.grid.size)
    print(f"This was the Breadth First algorithm on {game_name[:-4]}.\n")
    print(end - start)
    # # output_to_csv.output(rushhour.grid.size, breadth_first_solution.path, game_name, algorithm='Breadthfirst')


    # ------------------------------------- Run the depth first algorithm ------------------------------------
    # depth_first_class = DepthFirst(rushhour)
    # depth_first_solution = depth_first_class.run()
    # # visualisation.visualisation(depth_first_solution, rushhour.grid.size)
    # pygamegui.visualize(depth_first_solution, rushhour.grid.size)
    # print(f"This was the Depth First algorithm {game_name[:-4]}.\n")
    # # output_to_csv.output(rushhour.grid.size, depth_first_solution.path, game_name, algorithm='Depthfirst')


 # ------------------------------------- Run the A Star algorithm ------------------------------------
    start = time.time()
    Astar_class = Astar(rushhour)
    Astar_solution = Astar_class.run()
    end = time.time()
    visualisation.visualisation(Astar_solution, rushhour.grid.size)
    # pygamegui.visualize(Astar_solution, rushhour.grid.size)
    print(f"This was the A Star algorithm {game_name[:-4]}.\n")   
    # # output_to_csv.output(rushhour.grid.size, Astar_solution.path, game_name, algorithm='Astar')


# ------------------------------------- Run the Best First algorithm ------------------------------------
    # start = time.time()
    # best_first_class = BestFirst(rushhour)
    # best_first_solution = best_first_class.run()
    # end = time.time()
    # visualisation.visualisation(best_first_solution, rushhour.grid.size)
    # print(f"This was the Best First algorithm {game_name[:-4]}.\n")
    # print(end - start)   
    # output_to_csv.output(rushhour.grid.size, best_first_solution.path, game_name, algorithm='Random_Astar')


# ------------------------------------- Run the Greedy algorithm ------------------------------------
    # Greedy_class = Greedy(rushhour)
    # Greedy_solution = Greedy_class.run()
    # visualisation.visualisation(Greedy_solution, rushhour.grid.size)
    # print(f"This was the Greedy algorithm {game_name[:-4]}.\n")   

    # # visualisation.visualisation(depth_first_solution, rushhour.grid.size)
    # pygamegui.visualize(depth_first_solution, rushhour.grid.size)
    # print("This was the Depth First algorithm.\n")  
