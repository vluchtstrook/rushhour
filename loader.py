from classes import Car

def load_grid(filename):
    
    taken = {}

    with open(filename) as f:
        # skip header
        next(f)

        for line in f:
            line = line.rstrip()
            split_line = line.split(",")

            car_name = split_line[0]
            orientation = split_line[1]
            original_col = split_line[2]
            original_row = split_line[3]
            coordinate = (original_col, original_row)
            length = split_line[4]

            # add coordinate to list of taken spots
            taken[car_name] = coordinate

            # make Car object
            car = Car(car_name, orientation, length)

    return taken
