from fileinput import filename
from code.classes.rushhour import RushHour
import code.algorithms.randomise as randomise
import matplotlib.pyplot as plt
import numpy as np
import math

filename = 'data/Rushhour9X9_4.csv'

random_solutions = []
buckets = []
nr_solutions_per_bucket = []

for i in range(1000):
    rushhour = RushHour(filename)
    random_solution = randomise.random_algo(rushhour, rushhour.grid.size)
    random_solutions.append(random_solution.count)

max_solution_count = max(random_solutions)

nr_of_buckets = math.ceil(max_solution_count/1000)

for i in range(nr_of_buckets):
    count = 0
    for j in range(len(random_solutions)):
        if random_solutions[j] >= i*1000 and random_solutions[j] < (i+1)*1000:
            count += 1
    
    nr_solutions_per_bucket.append(count)
    buckets.append(i*1000)

print(nr_solutions_per_bucket)
print(buckets)

xpoints = np.array(buckets)
ypoints = np.array(nr_solutions_per_bucket)

plt.bar(xpoints, ypoints, fill = False, width= 4)
plt.show()