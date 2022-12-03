import string
from collections import Counter
from baseclass import BaseClass

class Day3Part1(BaseClass):

    def __init__(self):
        self.dt = self.get_data('day3_1')

    def get_common_letter(self, st):
        mid = len(st) // 2
        L, R = Counter(st[mid:]), Counter(st[:mid])
        return list(L & R)[0]

    def main(self):
        key = string.ascii_letters
        total = 0
        for line in self.dt:
            common = self.get_common_letter(line)
            idx = key.index(common) + 1
            total += idx
        print(total)

if __name__=="__main__":
    Day3Part1().main()