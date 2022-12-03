import string
from collections import Counter
from baseclass import BaseClass

class Day3Part2(BaseClass):

    def __init__(self):
        self.dt = self.get_data('day3_2')

    def get_common_letter(self, arr):
        if len(arr) != 3:
            print("WARNING")
        b1,b2,b3 = arr
        return list(Counter(b1) & Counter(b2) & Counter(b3))[0]

    def main(self):
        key = string.ascii_letters
        total = 0
        holder = []
        for line in self.dt:
            holder.append(line)
            if len(holder) == 3:
                common = self.get_common_letter(holder)
                print(common)
                total += key.index(common) + 1
                holder = []
        print(total)

if __name__=="__main__":
    Day3Part2().main()