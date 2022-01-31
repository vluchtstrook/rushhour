import pygame
from colour import Color

# constants
SCREEN_SIZE = 600

# colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def visualize(solution, size):
    blocksize = int(round((SCREEN_SIZE) / size))
    states = solution.path
    
    pygame.init()

    # set up screen
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption(f"Rushhour {blocksize} x {blocksize}")
    screen.fill(WHITE)

    running = True
    while running:

        # pass first state to randomly assign colours to all vehicles
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
    
    j = 0

    for x in range(size):
        for y in range(size):
            colour = car_colour[state[j + y]]

            pygame.draw.rect(screen, colour, (y * blocksize, x * blocksize, blocksize, blocksize))
    
        j += 6


def assign_colours(state):
    cars = set(state)

    car_colour = {}

    for car in cars:
        car_colour[car] = tuple(i * 255 for i in Color(pick_for=car).rgb)

    # X should always be red and _ should always be white
    car_colour['X'] = RED
    car_colour['_'] = WHITE

    return car_colour
