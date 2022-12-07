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
        self.all_directories = deque()
        self.memo = {}


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

                self.all_directories.appendleft(new_dir)
                
                if 'full_dir' not in node:
                    node['full_dir'] = old_full_dir + [new_dir]

                #self.all_directories.appendleft(node['full_dir'])                

                self.levels += 1

            # cd back
            elif cmd[0] == "$" and cmd[1] == "cd" and cmd[2] == ".." and self.levels > 1:
                old_dir = node['full_dir'][:]
                old_dir.pop()
                node = self.find_node(old_dir)
                self.levels -= 1


            # listing
            elif cmd[0] != "$" and cmd[0] != "dir":
                size, filename = cmd[0], cmd[1]
                if 'files' not in node:
                    node['files'] = []
                if filename not in node['files']:
                    node['files'].append(filename)
                    if 'size' not in node:
                        node['size'] = int(size)
                    else:
                        node['size'] += int(size)


    def find_node_exhaustive(self,node):
        stack = [self.trie]
        while stack:
            nd = stack.pop()
            if node in nd:
                return nd[node]
            for edge in nd:
                if edge not in ('full_dir', 'files', 'size'):
                    stack.append(nd[edge])
    
    def recurse(self, node):
        keys = [key for key in node if key not in ('full_dir', 'files', 'size')]
        print(keys)
        if not len(keys):
            if 'size' in node:
                return int(node['size'])
        for key in keys:
            self.memo[key] = self.recurse(node[key])

    def compile(self):
        memo = {}
        for node in self.all_directories:
            stack = [node]
            total = 0
            while stack:
                head = self.find_node_exhaustive(stack.pop())
                if 'size' in head:
                    total += int(head['size'])
                keys = [key for key in head if key not in ('full_dir', 'files', 'size')]
                for key in keys:
                    stack.append(head[key])
            memo[node] = total

    def main(self):
        self.form_trie()
        print(self.trie)
        self.compile()
        



if __name__=="__main__":
    Day7Part1().main()