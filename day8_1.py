"""
NOTES:

(1,1) - The top-left 5 is visible from the left and top.
(1,2) - The top-middle 5 is visible from the top and right.
(1,3) - The top-right 1 is not visible from any direction; for it to be visible,
(2,1) - The left-middle 5 is visible, but only from the right.
The center 3 is not visible from any direction; for it to be visible, 
The right-middle 3 is visible from the right.
In the bottom row, the middle 5 is visible, but the 3 and 4 are not.


"""
from baseclass import BaseClass

class Day8Part1(BaseClass):

    def __init__(self):
        self.dt = self.get_data('day8')

    def main(self):
        grid = self.dt
        visible = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if y in (0, len(grid)-1) or x in (0, len(grid[0])-1):
                    visible +=1
                else:
                    hidden = [False, False, False, False]
                    # to the left
                    for xx in range(0, x):
                        if grid[y][xx] >= grid[y][x]:
                            hidden[0] = True
                    # to the right
                    for xx in range(x+1, len(grid[0])):
                        if grid[y][xx] >= grid[y][x]:
                            hidden[1] = True
                    # up
                    for yy in range(0, y):
                        if grid[yy][x] >= grid[y][x]:
                            hidden[2] = True
                    # down
                    for yy in range(y+1, len(grid)):
                        if grid[yy][x] >= grid[y][x]:
                            hidden[3] = True
                    if sum(hidden) < 4:
                        visible += 1
        print(visible)







if __name__=="__main__":
    Day8Part1().main()