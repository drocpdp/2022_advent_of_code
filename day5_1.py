from baseclass import BaseClass

class Day5Part1(BaseClass):

    def __init__(self):
        self.dt = self.get_data('day5')

    def extract_instructions(self, st_inst):
        (_, tms, _, fr, _, to) = st_inst.split()
        return int(tms),int(fr)-1,int(to)-1

    def get_stacks(self):
        """ This is probably the most difficult part of the problem.
            Need a list of stacks.
            I'll be honest, I don't think we need to worry about dynamically
            extracting the starting stacks. I will just extract the moves.
            I will manually enter the stacks.


            [J]             [F] [M]            
            [Z] [F]     [G] [Q] [F]            
            [G] [P]     [H] [Z] [S] [Q]        
            [V] [W] [Z] [P] [D] [G] [P]        
            [T] [D] [S] [Z] [N] [W] [B] [N]    
            [D] [M] [R] [J] [J] [P] [V] [P] [J]
            [B] [R] [C] [T] [C] [V] [C] [B] [P]
            [N] [S] [V] [R] [T] [N] [G] [Z] [W]
             1   2   3   4   5   6   7   8   9             
        """
        return  [
                    list("NBDTVGZJ"),
                    list("SRMDWPF"),
                    list("VCRSZ"),
                    list("RTJZPHG"),
                    list("TCJNDZQF"),
                    list("NVPWGSFM"),
                    list("GCVBPQ"),
                    list("ZBPN"),
                    list("WPJ")
                ]

    def part1(self):
        stacks = self.get_stacks()
        for inst in self.dt:
            times, frm, to = self.extract_instructions(inst)
            for _ in range(times):
                stacks[to].append(stacks[frm].pop())

        print("".join(l[-1] for l in stacks))
     

if __name__=="__main__":
    Day5Part1().part1()





