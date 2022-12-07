"""
NOTES:
    -trie of dictionaries?
        -how to find parent when ../


"""
import json
from baseclass import BaseClass

class Day7Part1(BaseClass):

    def __init__(self):
        self.dt = self.get_data('day7_test')
        self.root = {}

    def find_node(self, node):
        if node is None:
            return node
        stack = [self.root]
        while stack:
            nd = stack.pop()
            if node in nd:
                return nd[node]
            else:
                for edge in nd:
                    if edge != "size":
                        stack.append(nd[edge])


    def main(self):

        """ create directory structure (trie) """
        curr = self.root
        curr_label = None

        for line in self.dt:
            cmd = line.split()

            if cmd[0] == "$":
                
                if cmd[1] == "cd":

                    to_dir = cmd[2]
                    
                    if to_dir != "..":
                        
                        if to_dir not in curr:
                            # set
                            curr[to_dir] = {}
                        curr = curr[to_dir]
                        curr['parent'] = curr_label
                        if 'label' not in curr:
                            curr['label'] = to_dir
                            curr_label = curr['label']

                    else: # cd ..
                        if curr['parent'] is not None:
                            curr = self.find_node(curr['parent'])
                            curr_label = curr['label']
                            if curr:
                                prev_label = curr['parent']
                            else:
                                curr = self.root
            else: # implied as ls
                if cmd[0] != 'dir':
                    if 'total_size' not in curr:
                        curr['total_size'] = 0
                    if 'files' not in curr: 
                        curr['files'] = []
                    if cmd[1] not in curr['files']:
                        # bet you there are multiple ls's 
                        curr['total_size'] += int(cmd[0])
                        curr['files'].append(cmd[1])


        print(json.dumps(self.root,indent=2))




if __name__=="__main__":
    Day7Part1().main()