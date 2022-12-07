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
        self.trie = {}
        self.levels = 0


    def find_node(self, file_struct):
        head = self.trie
        for f in file_struct:
            head = head[f]
        return head

    def form_trie(self):
        """ create directory structure (trie) """
        node = self.trie

        for line in self.dt:
            cmd = line.split()

            # cd forward
            if cmd[0] == "$" and cmd[1] == "cd" and cmd[2] != "..":
                new_dir = cmd[2]
                
                if 'full_dir' not in node:
                    node['full_dir'] = []

                if new_dir not in node:
                    old_full_dir = node['full_dir']
                    node[new_dir] = {}
                node = node[new_dir]
                
                if 'full_dir' not in node:
                    node['full_dir'] = old_full_dir + [new_dir]

                self.levels += 1

            # cd back
            if cmd[0] == "$" and cmd[1] == "cd" and cmd[2] == ".." and self.levels > 1:
                old_dir = node['full_dir'][:]
                old_dir.pop()
                node = self.find_node(old_dir)
                self.levels -= 1


    def main(self):
        self.form_trie()
        print(json.dumps(self.trie, indent=2))



if __name__=="__main__":
    Day7Part1().main()