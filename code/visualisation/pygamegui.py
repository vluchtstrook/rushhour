"""
pygamegui.py

Course: programmeertheorie
Team: vluchtstrook

This file contains three functions that (1) runs the pygame to visualize the path to a solution, (2) draws the grid for each
state with each vehicle and (3) assigns random colours to each vehicle.
This file is called from the main file (main.py).
"""


import pygame
from colour import Color
from code.classes.solution import Solution

# Constants.
SCREEN_SIZE = 600

# Colours.
WHITE = (255, 255, 255)
RED = (255, 0, 0)


def visualize(solution: Solution, size: int) -> None:
    """
    This function initialized the pygame and runs it while the user hasn't quit the game.
    """
    blocksize = int(round((SCREEN_SIZE) / size))
    states = solution.path
    
    pygame.init()

    # Set up screen.
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption(f"Rushhour {size} x {size}")
    screen.fill(WHITE)

    running = True
    while running:

        # Pass first state to randomly assign colours to all vehicles.
        car_colour = assign_colours(states[0])
        
        for state in states:
            draw_grid(screen, state, size, blocksize, car_colour)
            pygame.display.update()
            pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


def draw_grid(screen, state, size, blocksize, car_colour):
    """
    This function draws the grid (or gameboard).
    """
    
    j = 0

    for x in range(size):
        for y in range(size):
            colour = car_colour[state[j + y]]

            pygame.draw.rect(screen, colour, (y * blocksize, x * blocksize, blocksize, blocksize))
    
        j += size


def assign_colours(state):
    """
    This function assigns random colours to each vehicle on the grid (or gameboard), stores the combinations in a
    dictionary and returns it.
    """
    cars = set(state)

    car_colour = {}

    for car in cars:
        car_colour[car] = tuple(i * 255 for i in Color(pick_for=car).rgb)

    # X should always be red and _ should always be white.
    car_colour['X'] = RED
    car_colour['_'] = WHITE

    return car_colour
