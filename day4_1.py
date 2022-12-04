from baseclass import BaseClass

class Day4Part1(BaseClass):

    def __init__(self):
        dt = self.get_data('day4_1')
        total = 0
        for line in dt:
            range1,range2 = line.split(',')
            (l1,r1),(l2,r2) = range1.split('-'), range2.split('-')
            if ( int(l2)>=int(l1) and int(r2)<=int(r1) ) or ( int(l1)>=int(l2) and int(r1)<=int(r2)):
                total += 1
        print(total)


if __name__ == "__main__":
    Day4Part1()