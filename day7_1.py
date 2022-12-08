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

class Node:
    def __init__(self, val=None):
        self.val = val
        self.parent = None
        self.children = {} #directory name: object
        self.size = 0
        self.files = []


class Day7Part1(BaseClass):

    def __init__(self):
        self.dt = self.get_data('day7_test')
        self.head = Node()
        self.values = {}


    def main(self):
        curr = self.head

        for line in self.dt:
            cmd = line.split()

            # cd forward
            if cmd[0] == "$" and cmd[1] == "cd" and cmd[2] != "..":
                new_dir = cmd[2]
                if new_dir not in curr.children:
                    new_node = Node(new_dir)
                    new_node.parent = curr
                    curr.children[new_dir] = new_node
                    curr = new_node
                else:
                    curr = curr.children[new_dir]

            # cd back
            elif cmd[0] == "$" and cmd[1] == "cd" and cmd[2] == "..":
                if curr.parent is not None:
                    curr = curr.parent

            # listing
            elif cmd[0] != "$" and cmd[0] != "dir":
                size, filename = cmd[0], cmd[1]
                if filename not in curr.files:
                    curr.size += int(size)
                    curr.files.append(filename)
                    self.values[curr.val] = curr.size

        print(self.recurse(self.head))

    def recurse(self, node): 
        curr_val = node.size
        if not node.children:
            return int(curr_val)
        total = curr_val
        for key in node.children:
            total += self.recurse(node.children[key])
        return total



if __name__=="__main__":
    day7 = Day7Part1()
    day7.main()
