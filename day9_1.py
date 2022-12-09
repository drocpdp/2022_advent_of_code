"""
NOTES:

https://sites.pitt.edu/~jdnorton/Goodies/Chasing_the_light/

https://www.nationalgeographic.com/science/article/einstein-relativity-thought-experiment-train-lightning-genius

Einstein had already learned in physics class what a light beam was: a set of oscillating electric and 
magnetic fields rippling along at 186,000 miles a second, the measured speed of light. 
If he were to run alongside it at just that speed, Einstein reasoned, he ought to be able to look over 
and see a set of oscillating electric and magnetic fields hanging right next to him, seemingly stationary in space.

Yet that was impossible. For starters, such stationary fields would violate Maxwell’s 
equations, the mathematical laws that codified everything physicists at the time knew about 
electricity, magnetism, and light. The laws were (and are) quite strict: Any ripples in the 
fields have to move at the speed of light and cannot stand still—no exceptions.

Stationary light fields (thought experiment).

Someone standing on the embankment would measure the light beam’s speed to be the standard number, 
186,000 miles a second. But someone on the train would see it moving past at only 184,000 miles a second. 
If the speed of light was not constant, Maxwell’s equations would somehow have to look different inside 
the railway carriage, Einstein concluded, and the principle of relativity would be violated.

Einstein later illustrated this point with another thought experiment. Imagine that you once again have an 
observer standing on a railway embankment as a train goes roaring by. But this time, each end of the train 
is struck by a bolt of lightning just as the train’s midpoint is passing. Because the lightning strikes are the 
same distance from the observer, their light reaches his eye at the same instant. So he correctly says that they 
happened simultaneously.

Meanwhile, another observer on the train is sitting at its exact midpoint. From her perspective, 
the light from the two strikes also has to travel equal distances, and she will likewise measure the speed of 
light to be the same in either direction. But because the train is moving, the light coming from the lightning 
in the rear has to travel farther to catch up, so it reaches her a few instants later than the light coming from the 
front. Since the light pulses arrived at different times, she can only conclude the strikes were not simultaneous—that 
the one in front actually happened first.

I think this is the only theory needed to solve this problem.

The movement of the tail is determined by the movement, speed of the head. 
In a square, moving diagonally, if a square == 1 x 1, would be sqrt(2) which is > 1. (slower per unit of time)
diagonally is slower then up or down.

http://nehe.gamedev.net/tutorial/rope_physics/17006/

--So, if an old->new spot is along an axis, it will move the same move.
--If an old->new spot is diagonal, it must reside in a queue and will move the next time unit (relatively)
--If head is moving diagonal, and then left/right, the queue PLUS the "now-time" is added together.

Game theory (rope theory) akin to this. A slower computer cannot show every detail in units of time more microscopic
than a processor cycle. Thus, the reason the compensation for the diagonal movements snapping to the head.

force = -k * x
k: a constant to represent the stiffness of the spring
x: distance of the mass from the point it is bound to
force = spring tension (+f = further apart, -f = less tension thus closer together)
goal is to have force == 0 even if x (distance apart) is positive.


Oops, overcomplicated...
Simple:: --> If distance > 1, snap tail to a step behind in same direction

"""
import pandas
import numpy
import math
from baseclass import BaseClass

class Day9Part1(BaseClass):

    def __init__(self):
        self.dt = (line for line in self.get_data('day9'))


    def move_position(self, pos, direction):
        """ move from pos one space to R,L,U,D """
        movement = {
                        "R":(0,1),
                        "L":(0,-1), 
                        "U":(1,0), 
                        "D":(-1,0) 
                    }
        (y,x) = pos
        yy,xx = movement[direction]

        return (y+yy, x+xx)


    def get_distance(self, pt1, pt2):
        """ distance from two points, double/float """
        y1, x1 = pt1
        y2, x2 = pt2
        return math.sqrt(abs(y2 - y1)**2 + abs(x2 - x1)**2)


    def main(self):
        head, tail = (0,0), (0,0)
        prev = None
        visited = set()
        visited.add((0,0))
        
        for line in self.dt:
            move, times = line.split()
            for _ in range(int(times)):
                head = self.move_position(head, move)
                if prev is None:
                    prev = head
                else:
                    if self.get_distance(head, tail) > 1.5:
                        tail = prev
                        visited.add(tail)
                prev = head                    
        print(head)
        print(visited)
        print(len(visited))




if __name__=="__main__":
    Day9Part1().main()




