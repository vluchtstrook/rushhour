"""
solution.py

Course: programmeertheorie
Team: vluchtstrook

This file contains a class named Solution. It saves the path to a solution (where each grid in the path is saved as 
a string) and contains a counter for all the states that are created while finding a solution, as well as a counter for 
each unique state that is created while finding a solution.
An instance of the Solution class is created in the algorithm files (code/algorithms).
"""


class Solution:

    def __init__(self):
        self.path = []
        self.count_states = 0
        self.count_unique_states = 0
        