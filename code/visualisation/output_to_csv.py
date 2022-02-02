from typing import List
import pandas

def output(gridsize: int, path: List[str], game_name: str, algorithm: str) -> None:
    # use first state to obtain all carnames
    carnames = set(path[0])
    carnames.remove('_')
    cars = []
    moves = []

    # loop through all states and compare adjacent states
    for i in range(len(path) - 1):
        for car in carnames:
            if path[i + 1].index(car) - path[i].index(car) != 0:
                # move for horizontal cars
                move = path[i + 1].index(car) - path[i].index(car)

                # move for vertical cars 
                if move >= gridsize or move <= -gridsize:
                    move = move // gridsize
                
                cars.append(car)
                moves.append(move)

    series = pandas.Series(moves, index=cars)
    df = pandas.DataFrame({'move': series})
    df.index.name = 'car'

    # outputname not compatible with check 50
    # df.to_csv(f'code/visualisation/outputdata/{algorithm}_{game_name}')
    # outputname compatible with check50
    df.to_csv('code/visualisation/outputdata/output.csv')
