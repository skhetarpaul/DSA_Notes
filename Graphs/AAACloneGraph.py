"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''An important question. Same DFS algorithm will apply here, we just need to track reference of the nodes.
Hence, visited dictionary contains the new node reference. If node is not in visited-> create the node and 
append it to neighbours. Else, if already created, put that in neighbours list'''
import copy
from queue import Queue

class Solution:
    
    def cloneGraph(self, n: 'Node') -> 'Node':
        self.visited = {}
        if n is None:
            return None
        def recursion(node):
            clone_graph = Node(val = node.val, neighbors = [])
            self.visited[node.val] = clone_graph
            for nbr in node.neighbors:
                if nbr.val not in self.visited:
                    clone_graph.neighbors.append(recursion(nbr))
                else:
                    clone_graph.neighbors.append(self.visited[nbr.val])
            return clone_graph
        clone_head = recursion(n)
        return clone_head
        # for nbr in clone_head.neighbors:
        #     nbr.neighbours.append(clone)





     
