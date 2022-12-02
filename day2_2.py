#13509

from baseclass import BaseClass

class Day2Part2(BaseClass):

    def __init__(self):
        dt = self.get_data('day2_2')
        score = 0
        opp_shapes, results = set(), set() # just to confirm right values and 1-based

        for line in dt:
            shp, res = line.split()
            
            # one-based, one-based
            opp_shape, result = ord(shp)-ord('A') + 1, ord(res)-ord('X')+1
            
            # debugging
            results.add(result)
            opp_shapes.add(opp_shape)

            # add result to score
            score += ((result-1) * 3)
            
            # add our shape
            if result == 1: # you need to lose
                if (opp_shape - 1) == 0:
                    score += 3
                else:
                    score += (opp_shape - 1)
            elif result == 2: # you need to draw
                score += opp_shape
            elif result == 3: # you need to win
                if (opp_shape + 1) > 3:
                    score += 1
                else:
                    score += opp_shape + 1

        print(results, opp_shapes) # debugging
        print(score)


if __name__ == "__main__":
    Day2Part2()