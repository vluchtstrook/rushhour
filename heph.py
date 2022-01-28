from heapq import *
import math

heap = []
data = [(10,"kaas"), (3,"bhree"), (5,"five"), (7,"seven"), (9, "nine"), (2,"two"), (3, 'kaas')]
for item in data:
    heappush(heap, item)

print(heap)

print(heappop(heap))
print(heappop(heap))
print(heappop(heap))


# heappush(heap, (1, "one"))
finish_row_index = 6 // 2 if 6 % 2 == 0 else math.ceil(6 / 2)
print(finish_row_index)

# print(heap)