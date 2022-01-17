import pandas
from vehicle import Vehicle
from grid import Grid

def load_vehicles(filename):
    """
    Read all the grid data from the csv file into a dataframe.
    Load vehicle data from dataframe into Vehicle classes.
    """

    # vehicles = []
    vehicles = {}

    grid_data = pandas.read_csv(filename)
    grid_size = 0

    for index in grid_data.index: 
        # create Vehicle object
        vehicle = Vehicle(grid_data['car'][index], grid_data['orientation'][index], grid_data['col'][index] - 1, grid_data['row'][index] - 1, grid_data['length'][index])
        
        # append vehicles (by name) to vehicles dict
        vehicles[grid_data['car'][index]] = vehicle
        # vehicles.append(vehicle)

    # determine grid size
    grid_size = max(grid_data['col'].max(), grid_data['row'].max())
    
    # create Grid object
    grid = Grid(grid_size, vehicles)

    return grid
