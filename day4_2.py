from baseclass import BaseClass

class Day4Part2(BaseClass):

    def __init__(self):
        dt = self.get_data('day4_1')
        total = 0
        for line in dt:
            range1,range2 = line.split(',')
            (l1, r1), (l2, r2) = range1.split('-'), range2.split('-')
            l1, r1, l2, r2 = int(l1), int(r1), int(l2), int(r2)
            if r1 in range(l2,r2+1) or  r2 in range(l1,r1+1):
                total += 1
        print(total)


if __name__ == "__main__":
    Day4Part2()