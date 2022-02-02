"""
baseline.py

Course: programmeertheorie
Team: vluchtstrook

This file contains all code used to determine our baseline. It does not contain a function, but rather consecutive code
that runs our random algorithm and our first algorithm (breadth first) for a number of times and generates a barplot
with the results.
"""



from fileinput import filename
from code.algorithms.breadth_first import BreadthFirst
from code.algorithms.depth_first import DepthFirst
from code.classes.rushhour import RushHour
import code.algorithms.randomise as randomise
import matplotlib.pyplot as plt
import numpy as np
import math


filename = 'data/Rushhour6x6_1.csv'

random_solutions = []
buckets = []
nr_solutions_per_bucket = []

for _ in range(1000):
    rushhour = RushHour(filename)
    random_solution = randomise.random_algo(rushhour)
    random_solutions.append(random_solution.count_unique_states)

# for i in range(1000):
#     rushhour = RushHour(filename)
#     breadth_first_class = BreadthFirst(rushhour)
#     breadth_first_solution = breadth_first_class.run()
#     random_solutions.append(breadth_first_solution.count_states)

max_solution_count = max(random_solutions)

nr_of_buckets = math.ceil(max_solution_count/1000)

for i in range(nr_of_buckets):
    count = sum(
        random_solution_ >= i * 1000 and random_solution_ < (i + 1) * 1000
        for random_solution_ in random_solutions
    )

    nr_solutions_per_bucket.append(count)
    buckets.append(i*1000)

print(nr_solutions_per_bucket)
print(buckets)

xpoints = np.array(buckets)
ypoints = np.array(nr_solutions_per_bucket)

plt.bar(xpoints, ypoints, fill = False, width= 4)
plt.show()
