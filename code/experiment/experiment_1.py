from code.classes.rushhour import RushHour
import pandas as pd

from code.experiment.generate_solutions import GenerateSolutions

"""
Experiment_1:

Generate the X amount of shortest paths of the 9x9_4 puzzle, 

by executing a breadth_first untill an X amount of winning paths are found.
"""

# The puzzle of choice to retrieve a certain amount of winning states
filename = 'data/Rushhour9x9_4.csv'

rushhour = RushHour(filename)

# The amount winning solutions
amount_of_solutions = 400000

generate_solutions_class = GenerateSolutions(rushhour, amount_of_solutions)
generated_solutions = generate_solutions_class.run()

# Store the path length of the solutions to a dataframe
df = pd.DataFrame(generated_solutions, columns =['path'])

output_file_name = f'first_{amount_of_solutions}_win_states_9x9_4.csv'

# Create a csv file containing the data
df.to_csv(output_file_name)