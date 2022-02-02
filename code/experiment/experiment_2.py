import math
from code.algorithms.best_first import BestFirst
from code.classes.rushhour import RushHour
import pandas as pd

"""
Experiment_2: 
Generate a thousand Best First solutions to the 9x9_4 puzzle.

Compare the avarage of these thousand solutions to the solutions found in Experiment_1.

Calculate to which percenatage of the best X amount of solutions the average solution belongs.
"""

# The puzzle of choice to retrieve a certain amount of winning states
filename = 'data/Rushhour9x9_4.csv'
rushhour = RushHour(filename)

# Retrieve the data ouput from experiment_1
df = pd.read_csv('first_400000_win_states_9x9_4.csv')

length = df['path'].count()

best_first_solutions = []

# Generate a thousand solutions using with the Best First algorithm
i = 0
while i < 1000:
    best_first_class = BestFirst(rushhour)
    best_first_solution = best_first_class.run()
    i += 1
    print(i)

    # Store all path length of the solutions
    best_first_solutions.append(len(best_first_solution.path))

# Average solution of the thousand generated Best First solutions
mean_best_first_solution = math.ceil(sum(best_first_solutions)/len(best_first_solutions))

# The amount of solutions that are shorter than the avarage solution in the X shortest paths of the 9x9_4 puzzle
amount_of_shorter_solutions = df[df['path'] <= mean_best_first_solution]['path'].count()
percentage = (amount_of_shorter_solutions / df['path'].count()) * 100


print(f'Out of the first {length} best solutions')
print(f'The average solution path of best first belongs to the {percentage}% best answers.')