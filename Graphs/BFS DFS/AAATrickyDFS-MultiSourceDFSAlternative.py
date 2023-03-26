# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
'''This could be a standard approach as reaching to a common point from multiple nodes.
Now either you can perform DFS from every node and check if it reaches 0 or not or elsewise, you need to do the reverse.
By reverse, start from the root node, check if it is possible to move to other nodes, if yes check the path sign
If sign is positive-> then this edge needs to be changed
If sign is negative-> all good, move further'''

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0    
        adj = [[] for i in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(-1*u)
        visited = [0 for i in range(n)]

        def DFS(node):
            visited[node] = 1
            totalcount = 0
            
            for nbr in adj[node]:
                if not visited[abs(nbr)]:
                    totalcount+= DFS(abs(nbr)) + (nbr>0)
                    
            return totalcount
        return DFS(0)
        return self.res