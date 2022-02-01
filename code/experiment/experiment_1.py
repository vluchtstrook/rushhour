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

winning_statespace_class = WinStateSpace(rushhour, amount_of_winning_states)
winning_statespace_solution = winning_statespace_class.run()

# Store the path length of the solutions to a dataframe
df = pd.DataFrame(winning_statespace_solution, columns =['path'])

output_file_name = f'first_{amount_of_winning_states}_win_states_9x9_4.csv'

# Create a csv file containing the data
df.to_csv(output_file_name)



