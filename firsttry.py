import pandas

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

def load_vehicles(file):
    """
    Read all the grid data from the csv file into a dataframe
    Returns the dataframe.
    """
    grid_data = pandas.read_csv(file)

    for index in grid_data.index: 
        vehicles[grid_data['car'][index]] = Verhicle(grid_data['car'][index], grid_data['orientation'][index],grid_data['col'][index],grid_data['row'][index],grid_data['length'][index])

def span_grid():
    for vehicle in vehicles:
        for l in range(vehicles[vehicle].length):
            if vehicles[vehicle].orientation == 'H':
                grid[vehicles[vehicle].row - 1][vehicles[vehicle].col + l - 1] = vehicles[vehicle].car
            else:
                grid[vehicles[vehicle].row + l - 1][vehicles[vehicle].col - 1] = vehicles[vehicle].car

def print_grid():
    print()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = '')
            print(' ', end='')
        if i == 2:
            print('<', end='')
        print()

def display_grid():
    span_grid()
    print_grid()

def delete_pisition(vehicle_name):
    for l in range(vehicles[vehicle_name].length):
        if vehicles[vehicle_name].orientation == 'H':
            grid[vehicles[vehicle_name].row - 1][vehicles[vehicle_name].col + l - 1] = '_'
        else:
            grid[vehicles[vehicle_name].row + l - 1][vehicles[vehicle_name].col - 1] = '_'

def valid_move(vehicle_name, direction):
    if direction == 'left' and vehicles[vehicle_name].orientation == 'H' and vehicles[vehicle_name].col != 1 and grid[vehicles[vehicle_name].row - 1][vehicles[vehicle_name].col - 2] == '_':
        return True
    
    if direction == 'right' and vehicles[vehicle_name].orientation == 'H' and vehicles[vehicle_name].col + vehicles[vehicle_name].length <= 6 and grid[vehicles[vehicle_name].row - 1][vehicles[vehicle_name].col - 1 + vehicles[vehicle_name].length] == '_':
        return True
    
    if direction == 'up' and vehicles[vehicle_name].orientation == 'V' and vehicles[vehicle_name].row != 1 and grid[vehicles[vehicle_name].row - 2][vehicles[vehicle_name].col - 1] == '_':
        return True

    if direction == 'down' and vehicles[vehicle_name].orientation == 'V' and vehicles[vehicle_name].row + vehicles[vehicle_name].length <= 6 and grid[vehicles[vehicle_name].row - 1 + vehicles[vehicle_name].length][vehicles[vehicle_name].col - 1] == '_':
        return True

    return False

def move(vehicle_name, direction):
    if direction == 'left':
        if valid_move(vehicle_name, direction):
            delete_pisition(vehicle_name)
            vehicles[vehicle_name].col -= 1
        else:
            print()
            print('Not a valid move')

    if direction == 'right':
        if valid_move(vehicle_name, direction):
            delete_pisition(vehicle_name)
            vehicles[vehicle_name].col += 1
        else:
            print()
            print('Not a valid move')

    if direction == 'down':
        if valid_move(vehicle_name, direction):
            delete_pisition(vehicle_name)
            vehicles[vehicle_name].row += 1
        else:
            print()
            print('Not a valid move')

    if direction == 'up':
        if valid_move(vehicle_name, direction):
            delete_pisition(vehicle_name)
            vehicles[vehicle_name].row -= 1
        else:
            print()
            print('Not a valid move')



## Main ##

# Load all vehicles
load_vehicles('Rushhour6x6_1.csv')

# Span the vehicles within grid
span_grid()

# Display the grid
print_grid()

print()

# Move A to the right
move('A', 'left')
display_grid()
move('C', 'left')
display_grid()
move('B', 'left')
display_grid()
move('B', 'right')
display_grid()
move('B', 'right')
display_grid()

display_grid
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





# # Span the vehicles within grid
# span_grid()

# # Display the grid
# print_grid()

# print()
