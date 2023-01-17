#Note that if you can somehow find the minimum time to travel all subnpodes, ypou can add that easily to root and get answer. Intuition for using DFS and recursion. Rest all is a simple technique and handling edge cases. Look at the code.


from ast import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        visited = [0 for i in range(n)]
        adj = [set() for i in range(n)]
        for u, v in edges:
            adj[v].add(u)
            adj[u].add(v)

        def DFS(node):
            visited[node] = True
            sec = 0
            for nbr in adj[node]:
                if visited[nbr]!=True:
                    sec+=DFS(nbr)
            print("Node {} has DFS {}".format(node, sec))
            if sec>0:
                return sec+2 if node!=0 else sec
            else:
                if hasApple[node]:
                    return 2 if node!=0 else 0
                else:
                    return 0
        return DFS(0)