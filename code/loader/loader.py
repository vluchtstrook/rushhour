import pandas
from code.classes.vehicle import Vehicle
from code.classes.grid import Grid

def load_vehicles(filename):
    """
    Read all the grid data from the csv file into a dataframe.
    Load vehicle data from dataframe into Vehicle classes.
    """
    # Load data from the csv file
    grid_data = pandas.read_csv(filename)

    # Dictionary to store all vehicles
    vehicles = {}

    # Store all vehicle keys
    vehicle_names = []

    for index in grid_data.index: 
        # Create Vehicle object and add it (by name) to the dictionary
        vehicles[grid_data['car'][index]] = Vehicle(grid_data['car'][index], grid_data['orientation'][index], grid_data['length'][index])
        
        # Store all vehicle keys
        vehicle_names.append(grid_data['car'][index])

    return vehicles, vehicle_names

def load_grid(filename):
    
    # Load data from the csv file
    grid_data = pandas.read_csv(filename)

    # determine grid size
    grid_size = max(grid_data['col'].max(), grid_data['row'].max())

    # 2x2 array to respresent the grid
    grid_array = [['_' for i in range(grid_size)] for j in range(grid_size)]

    for index in grid_data.index: 
        # set the vehicles inside the 2x2 array, which represents the grid
        for i in range(grid_data['length'][index]):
            if grid_data['orientation'][index] == 'H':
                grid_array[grid_data['row'][index] - 1][grid_data['col'][index] + i - 1] = grid_data['car'][index]
            else:
                grid_array[grid_data['row'][index] + i - 1][grid_data['col'][index] - 1] = grid_data['car'][index]

    # create Grid object
    grid = Grid(grid_size, grid_array)

    return grid