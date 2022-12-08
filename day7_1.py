"""
NOTES:
    -trie of dictionaries
    -each trie has
        -ds (directory structure) which is a stack
            -popped to move up directory
            -when created, the dir pushed to ds
        -size (file size)
        -files (list) to ensure uniqueness
            -edge case: ls directory again
                -ls is where i compile the files and sizes for that directory

"""

from collections import deque
import copy
import json
from baseclass import BaseClass

class Day7Part1(BaseClass):

    def __init__(self):
        self.dt = self.get_data('day7')
        self.tree = {}
        """ 
            {
                '[name]':{
                            'size': int,
                            'parent': dir ,
                            'filenames':[]

                            },
                ...
            }
        """
        self.mapping = {}

    def main(self):
        curr = self.tree
        curr_listing = None

        for line in self.dt:
            cmd = line.split()

            # cd forward

            if cmd[0] == "$" and cmd[1] == "cd" and cmd[2] != "..":
                new_dir = cmd[2]

                if new_dir not in curr:
                    curr[new_dir] = {}
                    curr = curr[new_dir]
                    self.mapping[new_dir] = curr
                    curr['size'] = 0
                    curr['parent'] = curr_listing
                    curr_listing = new_dir
                    curr['filenames'] = []

            # cd back

            elif cmd[0] == "$" and cmd[1] == "cd" and cmd[2] == "..":
                curr = self.mapping[curr['parent']]

           # listing

            elif cmd[0] != "$" and cmd[0] != 'dir':
                size, filename = int(cmd[0]), cmd[1]
                if filename not in curr['filenames']:
                    curr['size'] += size
                    curr['filenames'].append(filename)





        #print(json.dumps(self.tree, indent=2))

        answer = 0
        for dirs in self.mapping:
            total = 0
            stack = [dirs]
            while stack:
                dir_name = stack.pop()
                directory = self.mapping[dir_name]
                total += directory['size']
                for edge in directory:
                    if edge not in ('filenames','size','parent'):
                        stack.append(edge)
            print(dirs, total)
            if total <= 100000:
                answer += total
        print(answer)






if __name__=="__main__":
    day7 = Day7Part1()
    day7.main()
    # 1137314 - too low
