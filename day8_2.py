from collections import defaultdict
from functools import reduce
from baseclass import BaseClass

class Day8Part2(BaseClass):

    def __init__(self):
        self.dt = self.get_data('day8')

    def monotonic(self, lst):
        """ monotonic stack. Include first element (view point).
            Implemented with 2-pointer b/c of the fixed building height from vantage point.
            (Need a comparison point).
            Compensate by subtracting 1 at return

            if item < building and before higher point, count it
            if item < building and < higher point but after higher point, don't count it
            if item > building and > higher point, set new higher point, count higher point + 1
        """
        size = lst[0]
        for i in range(1, len(lst)):
            if lst[i] >= size:
                return i - 0
        return len(lst) - 1



    def main(self):
        grid = self.dt
        total = 0
        max_score = 0
        tree_checker = defaultdict(list)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # left
                subtotal = self.monotonic(grid[y][0:x+1][::-1])
                tree_checker[(y,x)].append(subtotal)
                # right
                subtotal = self.monotonic(grid[y][x:len(grid[0])])
                tree_checker[(y,x)].append(subtotal)
                # top
                subtotal = self.monotonic([grid[yy][x] for yy in range(0,y+1)][::-1])
                tree_checker[(y,x)].append(subtotal)
                # bottom
                subtotal = self.monotonic([grid[yy][x] for yy in range(y, len(grid))])
                tree_checker[(y,x)].append(subtotal)
        for tree in tree_checker:
            matrix = tree_checker[tree]
            #matrix = [val if val !=0 else 1 for val in matrix]
            total = reduce(lambda a,b: a*b, matrix)
            print(tree, matrix, total)
            max_score = max(max_score, total)
        print(total)
        print(max_score)

if __name__ == "__main__":
    Day8Part2().main()

# 383632 - too low
# 444600 - too high
# 410400

