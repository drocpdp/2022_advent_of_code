"""
NOTES:
    -In the protocol being used by the Elves, the start of a packet is indicated 
        by a sequence of four characters that are all different.
    -First sequence of four characters that are all unique
    -Sliding window

"""
from collections import Counter
from baseclass import BaseClass

class Day6Part1(BaseClass):

    def __init__(self):
        """ sliding window """
        dt = self.get_data('day6_1')[0]

        holder = Counter()
        
        for i, ch in enumerate(dt):
            # add 
            holder.update(ch)

            # get 4 initial characters in
            if i < 4:
                continue

            # remove earliest char
            holder.subtract(dt[i-4])

            # 4 unique chars
            if len(set(holder.elements())) == 4:
                print(i+1)
                return

if __name__=="__main__":
    Day6Part1()