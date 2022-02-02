"""
depth_first.py

Course: programmeertheorie
Team: vluchtstrook

This file contains the depth first algorithm. It runs on the Rushhour class and inherits from the Breadth First Class 
(code/algorithms/breadth_first.py). This class contains a method that gets the last state of the queue.
This algorithm is called from the main file (main.py).
"""


from code.algorithms.breadth_first import BreadthFirst 


class DepthFirst(BreadthFirst):
    """
    This algorithm creates a stack of possible states of the game. Only unique states are in the stack.
    """

    def get_next_state(self) -> str:
        """
        This method gets the last added state from the stack.
        """
        return self.queue.pop()