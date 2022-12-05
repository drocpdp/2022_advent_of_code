from baseclass import BaseClass
from day5_1 import Day5Part1
from collections import deque

class Day5Part2(Day5Part1):

    def __init__(self):
        self.dt = self.get_data('day5')

    def part2(self):
        stacks = self.get_stacks()

        for inst in self.dt:
            dq = deque([])            
            tms, fr, to = self.extract_instructions(inst)

            for _ in range(tms):
                dq.appendleft(stacks[fr].pop())

            stacks[to].extend(list(dq))        

        print("".join(l[-1] for l in stacks))           

if __name__=="__main__":
    Day5Part2().part2()    