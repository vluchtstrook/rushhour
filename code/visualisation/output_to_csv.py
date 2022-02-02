"""
output_to_csv.py

Course: programmeertheorie
Team: vluchtstrook

This file contains a function that creates an outputfile for any solution path, containing all consecutive moves to the 
solution.
This function is called from the main file (mainfile.py).
"""


from typing import List
import pandas


def output(gridsize: int, path: List[str], game_name: str, algorithm: str) -> None:
    """
    This function loops through all states that lead to a solution, and adds each consecutive move to a dataframe.
    The dataframe is converted to a csv file.
    """
    # Use first state to obtain all carnames.
    carnames = set(path[0])
    carnames.remove('_')
    cars = []
    moves = []

    # Loop through all states and compare adjacent states.
    for i in range(len(path) - 1):
        for car in carnames:
            if path[i + 1].index(car) - path[i].index(car) != 0:
                # Horizontal cars.
                move = path[i + 1].index(car) - path[i].index(car)

                # Vertical cars.
                if move >= gridsize or move <= -gridsize:
                    move = move // gridsize
                
                cars.append(car)
                moves.append(move)

    series = pandas.Series(moves, index=cars)
    df = pandas.DataFrame({'move': series})
    df.index.name = 'car'

    # Outputname not compatible with check50.
    # df.to_csv(f'code/visualisation/outputdata/{algorithm}_{game_name}')

    # Outputname compatible with check50.
    df.to_csv('code/visualisation/outputdata/output.csv')
