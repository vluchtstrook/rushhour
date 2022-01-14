import pandas
import random

vehicles = {}

class Verhicle():

    def __init__(self, car, orientation, col, row, length):
        self.car = car
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length

# Great 6x6 empty grid
grid = [['_','_','_','_','_','_'],
        ['_','_','_','_','_','_'],
        ['_','_','_','_','_','_'],
        ['_','_','_','_','_','_'],
        ['_','_','_','_','_','_'],
        ['_','_','_','_','_','_']]

# Meant to store all vehicle names, is filled within load_vehicles function.
vehicle_types = []

# Contains all possible moves.
move_types = ['left', 'right', 'up', 'down']

def load_vehicles(file):
    """
    Read all the grid data from the csv file into a dataframe.
    Load vehicle data from dataframe into Vehicle classes.
    """
    grid_data = pandas.read_csv(file)

    for index in grid_data.index: 
        vehicles[grid_data['car'][index]] = Verhicle(grid_data['car'][index], grid_data['orientation'][index], grid_data['col'][index] - 1, grid_data['row'][index] - 1, grid_data['length'][index])
        vehicle_types.append(grid_data['car'][index])

def span_grid():
    """
    Load the vehicles names, length and position into the grid (2x2 list).
    """
    for vehicle in vehicles:
        for l in range(vehicles[vehicle].length):
            if vehicles[vehicle].orientation == 'H':
                grid[vehicles[vehicle].row][vehicles[vehicle].col + l] = vehicles[vehicle].car
            else:
                grid[vehicles[vehicle].row + l][vehicles[vehicle].col] = vehicles[vehicle].car

def print_grid():
    """
    Print the current grid to the user.
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = '')
            print(' ', end='')
        if i == 2:
            print('<', end='')
        print()
    print()

def display_grid():
    """
    Span & print the grid.
    """ 
    span_grid()
    print_grid()

def delete_pisition(vehicle_name):
    """
    Delete the old position of a vehicle that is being moved within the grid.
    """
    for l in range(vehicles[vehicle_name].length):
        if vehicles[vehicle_name].orientation == 'H':
            grid[vehicles[vehicle_name].row][vehicles[vehicle_name].col + l] = '_'
        else:
            grid[vehicles[vehicle_name].row + l][vehicles[vehicle_name].col] = '_'

def valid_move(vehicle_name, direction):
    """
    Check wheter move is possible.
    """
    if direction == 'left' and vehicles[vehicle_name].orientation == 'H' and vehicles[vehicle_name].col != 0 and grid[vehicles[vehicle_name].row][vehicles[vehicle_name].col - 1] == '_':
        return True
    
    if direction == 'right' and vehicles[vehicle_name].orientation == 'H' and vehicles[vehicle_name].col + vehicles[vehicle_name].length <= 5 and grid[vehicles[vehicle_name].row][vehicles[vehicle_name].col + vehicles[vehicle_name].length] == '_':
        return True
    
    if direction == 'up' and vehicles[vehicle_name].orientation == 'V' and vehicles[vehicle_name].row != 0 and grid[vehicles[vehicle_name].row - 1][vehicles[vehicle_name].col] == '_':
        return True

    if direction == 'down' and vehicles[vehicle_name].orientation == 'V' and vehicles[vehicle_name].row + vehicles[vehicle_name].length <= 5 and grid[vehicles[vehicle_name].row + vehicles[vehicle_name].length][vehicles[vehicle_name].col] == '_':
        return True

    return False

def move(vehicle_name, direction):
    """
    Try to move a vehicle.
    """
    if direction == 'left':
        if valid_move(vehicle_name, direction):
            delete_pisition(vehicle_name)
            vehicles[vehicle_name].col -= 1
            return True
        return False

    if direction == 'right':
        if valid_move(vehicle_name, direction):
            delete_pisition(vehicle_name)
            vehicles[vehicle_name].col += 1
            return True
        return False

    if direction == 'down':
        if valid_move(vehicle_name, direction):
            delete_pisition(vehicle_name)
            vehicles[vehicle_name].row += 1
            return True
        else:
            return False

    if direction == 'up':
        if valid_move(vehicle_name, direction):
            delete_pisition(vehicle_name)
            vehicles[vehicle_name].row -= 1
            return True
        else:
            return False

def random_algo():
    """
    Randomly try to move vehicles around untill a solution state has been found.
    """
    count = 1
    while grid[2][5] != 'X':
        random_vehicle = random.choice(vehicle_types)
        random_move = random.choice(move_types)

        if move(random_vehicle, random_move) == True:
            print(f'{random_vehicle} moved to {random_move}')
            display_grid()

        else:
            print()
            print('Not a valid move')

        count += 1
    print(f'It took {count} random steps.')


## Main ##
load_vehicles('Rushhour6x6_1.csv')
display_grid()
random_algo()


# Correct solution to puzzle 1
# move('A', 'left')
# move('C', 'left')
# move('J', 'left')
# move('G', 'up')
# move('G', 'up')
# move('L', 'up')
# move('L', 'up')
# move('J', 'left')
# move('J', 'left')
# move('I', 'down')
# move('I', 'down')
# move('H', 'right')
# move('E', 'down')
# move('D', 'left')
# move('E', 'down')
# move('E', 'down')
# move('H', 'left')
# move('I', 'up')
# move('I', 'up')
# move('I', 'up')
# move('H', 'right')
# move('E', 'up')
# move('E', 'up')
# move('J', 'right')
# move('J', 'right')
# move('J', 'right')
# move('L', 'down')
# move('X', 'right')
# move('E', 'down')
# move('X', 'right')
# move('X', 'right')
# move('G', 'down')
# move('B', 'left')
# move('I', 'up')
# move('X', 'right')

print()
