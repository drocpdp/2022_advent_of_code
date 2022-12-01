"""
NOTES:

-each elf: how many calories
-return elf carrying most calories


"""

from baseclass import BaseClass
import heapq

class Day1Part1(BaseClass):

    def __init__(self):
        dt = self.get_data('day_1_1')
        pq = []
        curr_tot = 0
        for i, line in enumerate(dt):
            if line:
                curr_tot += int(line)
            else:
                heapq.heappush(pq, (-curr_tot, i))
                curr_tot = 0
        tot, elf = heapq.heappop(pq)
        print(-tot, elf)


if __name__== "__main__":
    Day1Part1()