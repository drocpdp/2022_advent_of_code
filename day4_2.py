from baseclass import BaseClass

class Day4Part2(BaseClass):

    def __init__(self):
        dt = self.get_data('day4_1')
        total = 0
        for line in dt:
            # extract
            range1,range2 = line.split(',')
            (l1,r1),(l2,r2) = range1.split('-'), range2.split('-')

            # easiest to just sort by starting range of each
            ranges = sorted([(int(l1),int(r1)),(int(l2),int(r2))])
            
            (l1,r1),(l2,r2) = ranges
            
            # within range?
            if r1>=l2:
                total += 1

        print(total)


if __name__ == "__main__":
    Day4Part2()