"""
loader.py

Course: programmeertheorie
Team: vluchtstrook

This file contains two loader functions that (1) load all vehicles from a csv file and (2) loads the playing board (grid).
This file is called from the Rushhour Class (rushhour.py).
"""


from typing import Dict, List
import pandas
from code.classes.vehicle import Vehicle
from code.classes.grid import Grid


def load_vehicles(filename: str) -> tuple[Dict[str, Vehicle], List[str]]:
    """
    This function loads vehicle data from a csv file and stores it in instances of the Vehicle class. It returns
    a dictionary of vehicles and a list of vehicle names.
    """
    
    # Load data from the csv file.
    grid_data = pandas.read_csv(filename)

    # Dictionary to store all vehicles.
    vehicles = {}

    # Store all vehicle names.
    vehicle_names = []

    for index in grid_data.index: 
        
        # Create Vehicle object and add it (by name) to dictionary.
        vehicles[grid_data['car'][index]] = Vehicle(grid_data['car'][index], grid_data['orientation'][index], grid_data['length'][index])
        
        # Store all vehicle names.
        vehicle_names.append(grid_data['car'][index])

    return vehicles, vehicle_names


def load_grid(filename: str) -> Grid:
    """
    This function loads grid data from a csv file and stores it in instances of the Grid class. The Grid instance is returned.
    """
    
    # Load data from the csv file.
    grid_data = pandas.read_csv(filename)

    # Determine grid size.
    grid_size = max(grid_data['col'].max(), grid_data['row'].max())

    # 2x2 array to respresent the grid.
    grid_array = [['_' for _ in range(grid_size)] for _ in range(grid_size)]

    for index in grid_data.index: 

        # Put vehicles inside the 2x2 array.
        for i in range(grid_data['length'][index]):
            if grid_data['orientation'][index] == 'H':
                grid_array[grid_data['row'][index] - 1][grid_data['col'][index] + i - 1] = grid_data['car'][index]
            else:
                grid_array[grid_data['row'][index] + i - 1][grid_data['col'][index] - 1] = grid_data['car'][index]

    return Grid(grid_size, grid_array)
