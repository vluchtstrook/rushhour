import math
from code.algorithms.best_first import BestFirst
from code.classes.rushhour import RushHour
import pandas as pd

from code.experiment.winningstatespace import WinStateSpace

"""
Experiment_1:

Retrieve the X shortest paths of the 9x9_4 puzzle by executing a breadth_first untill a X amount of winning paths are found.

Compare the best X amount of solutions to the average path length of the Best First algorithm.

For the average path length of Best First it is ran a thousand times.

"""

# The puzzle of choice to retrieve a certain amount of winning states
filename = 'data/Rushhour9x9_4.csv'

rushhour = RushHour(filename)

# The amount winning solutions
amount_of_winning_states = 400000

# winning_statespace_class = WinStateSpace(rushhour, amount_of_winning_states)
# winning_statespace_solution = winning_statespace_class.run()

# # Store the path length of the solutions to a dataframe
# df = pd.DataFrame(winning_statespace_solution, columns =['path'])

# output_file_name = f'first_{amount_of_winning_states}_win_states_9x9_4.csv'

# # Create a csv file containing the data
# df.to_csv(output_file_name)

df = pd.read_csv('first_400000_win_states_9x9_4.csv')

rushhour = RushHour(filename)

best_first_solutions = []

i = 0
while i < 1000:
    best_first_class = BestFirst(rushhour)
    best_first_solution = best_first_class.run()
    best_first_solutions.append(len(best_first_solution.path))

mean_best_first_path_length = math.ceil(sum(best_first_solutions)/len(best_first_solutions))

amount_of_shorter_paths = df[df['path'] <= mean_best_first_path_length]['path'].count()

percentage = (amount_of_shorter_paths / df['path'].count())*100


print(f'Out of the first {amount_of_winning_states} best solutions')
print(f'The average solution path of best first belongs to the {percentage}\% best answers.')



