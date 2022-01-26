import pygame
import random

# constants
SCREEN_SIZE = 600
# BLOCKSIZE = int(round((SCREEN_SIZE) / GRID))

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
RED = (255, 0, 0)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
RGB = (r, g, b)

SIENNA = (160, 82, 45)
BLUE = (25, 25, 112)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
SILVER = (192, 192, 192)
TOMATO = (255, 99, 71)
WHEAT = (245, 222, 179)
ROSE = (255, 228, 225)
GOLD = (218, 165, 32)


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
        
        for state in states:
            draw_grid(screen, state, size, blocksize)
            pygame.display.update()
            pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


def draw_grid(screen, state, size, blocksize):
    j = 0

    for x in range(size):
        for y in range(size):
            if state[j + y] == 'A':
                colour = SIENNA
            elif state[j + y] == 'B':
                colour = BLUE
            elif state[j + y] == 'C':
                colour = PINK
            elif state[j + y] == 'D':
                colour = CYAN
            elif state[j + y] == 'E':
                colour = PURPLE
            elif state[j + y] == 'F':
                colour = TEAL
            elif state[j + y] == 'G':
                colour = MAROON
            elif state[j + y] == 'H':
                colour = OLIVE
            elif state[j + y] == 'I':
                colour = SILVER
            elif state[j + y] == 'J':
                colour = TOMATO
            elif state[j + y] == 'K':
                colour = WHEAT
            elif state[j + y] == 'L':
                colour = ROSE
            elif state[j + y] == 'X':
                colour = RED
            else:
                colour = WHITE

            pygame.draw.rect(screen, colour, (y * blocksize, x * blocksize, blocksize, blocksize))
    
        j += 6

