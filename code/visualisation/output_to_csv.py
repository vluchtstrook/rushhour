import pandas

def output(gridsize, path, game_name, algorithm):
    
    first_state = path[0]
    last_state = path[-1]

    cars = set(first_state)
    cars.remove('_')
    difference_dict = {}

    for car in cars:
        # difference for horizontal cars
        difference = last_state.index(car) - first_state.index(car)

        # difference for vertical cars 
        if difference >= gridsize or difference <= -gridsize:
            difference = difference // gridsize
        
        difference_dict[car] = difference

    series = pandas.Series(difference_dict, index=difference_dict.keys())
    df = pandas.DataFrame({'move': series})
    df.index.name = 'car'
    df = df.sort_index()
    df.to_csv(f'code/visualisation/outputdata/{algorithm}_{game_name}')
