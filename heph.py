from heapq import *
import math
from re import L
from code.algorithms.best_first import BestFirst
from code.algorithms.randomise import random_winning_state

from code.classes.rushhour import RushHour

# heap = []
# data = [(10,"kaas"), (3,"bhree"), (5,"five"), (7,"seven"), (9, "nine"), (2,"two"), (3, 'kaas')]
# for item in data:
#     heappush(heap, item)

# print(heap)

# print(heappop(heap))
# print(heappop(heap))
# print(heappop(heap))


# # heappush(heap, (1, "one"))
# finish_row_index = 6 // 2 if 6 % 2 == 0 else math.ceil(6 / 2)
# print(finish_row_index)

rushhour = RushHour('data/Rushhour6x6_1.csv')

random_astar = BestFirst(rushhour)

random_astar.prefered_position(rushhour.grid, rushhour)

# print(heap)

# print()