import pandas
from code.classes.vehicle import Vehicle
from code.classes.grid import Grid

def load_vehicles(filename):
    """
    Read all the grid data from the csv file into a dataframe.
    Load vehicle data from dataframe into Vehicle classes.
    """

    grid_data = pandas.read_csv(filename)

    vehicles = {}
    vehicle_names = []

    for index in grid_data.index: 
        # create Vehicle object
        vehicles[grid_data['car'][index]] = Vehicle(grid_data['car'][index], grid_data['orientation'][index], grid_data['length'][index])
        
        # append vehicles (by name) to vehicles dict
        vehicle_names.append(grid_data['car'][index])

    return vehicles, vehicle_names

def load_grid(filename):

    grid_data = pandas.read_csv(filename)

    # determine grid size
    grid_size = max(grid_data['col'].max(), grid_data['row'].max())

    # 2x2 array to respresent the grid
    new_grid = [['_' for i in range(grid_size)] for j in range(grid_size)]

    for index in grid_data.index: 
        # set the vehicles inside the 2x2 array, which represents the grid
        for i in range(grid_data['length'][index]):
            if grid_data['orientation'][index] == 'H':
                new_grid[grid_data['row'][index] - 1][grid_data['col'][index] + i - 1] = grid_data['car'][index]
            else:
                new_grid[grid_data['row'][index] + i - 1][grid_data['col'][index] - 1] = grid_data['car'][index]

    # create Grid object
    grid = Grid(grid_size, new_grid)

    return grid