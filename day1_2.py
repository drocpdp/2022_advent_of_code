import heapq
from baseclass import BaseClass

class Day1Part2(BaseClass):

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
        answer = 0
        for _ in range(3):
            tot, elf = heapq.heappop(pq)
            answer += -tot
        print(answer)


if __name__== "__main__":
    Day1Part2()