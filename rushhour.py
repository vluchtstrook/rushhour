from loader import load_grid

filename = "gameboards/Rushhour6x6_1.csv"


class RushHour:
    
    def __init__(self, filename):
        # dictionary of taken spots per car
        self.taken = load_grid(filename)
        # set of taken spots in total
        self.taken_total = set(self.taken.values())
    
    def possible_moves(self):
        # check all possible moves
        # add extra coordinates per car (use orientation)


        pass

    def move(self):
        # check if move is possible, then execute
        pass


if __name__ == "__main__":
    load_grid(filename)