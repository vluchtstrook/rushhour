from code.algorithms.breadth_first import BreadthFirst 


class DepthFirst(BreadthFirst):
    """
    A Depth First algorithm.

    Almost all of the functions are eqal to those of the BreadthFirst class, which is why
    we use that as a parent class.
    """

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        For Depth First we need the last one added to the list; we use a stack.
        """
        return self.queue.pop()