"""
NOTES

Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won).

constant - shape you chose, no matter of outcome
Rock(A): 1, Paper(B): 2, Scissors(C): 3

Opponent:
Rock(X), Paper(Y), Scissors(Z)

rock > scissors > paper
scissors > paper > rock
paper > rock > scissors
wow, circular!
starting point of ABC XYZ is rock

only 2 apart, which could easily translate into distane * 3
0 lost, 3 draw, 6 win

enumerate 
rock - 1
paper - 2
scissors - 3


tc:
    -scissors vs rock

"""

from baseclass import BaseClass

class Day2Part1(BaseClass):

    def __init__(self):
        dt = self.get_data('day2_1')
        # key (your POV)
        wins = { 1:3, 2:1, 3:2 }
        score = 0
        for line in dt:
            p1, p2 = line.split()
            p1, p2 = ord(p1)-ord('A') + 1, ord(p2)-ord('X') + 1
            # your shape
            score += p2
            # faceoff
            if p1 == p2:
                score += 3
            elif wins[p2] == p1:
                score += 6
        print(score)



if __name__ == "__main__":
    Day2Part1()