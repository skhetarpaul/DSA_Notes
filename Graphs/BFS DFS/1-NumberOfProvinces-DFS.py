# https://leetcode.com/problems/number-of-provinces/submissions/844578559/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)

        def DFS(node):
            visited[node] = 1
            for nbr in adj[node]:
                if not visited[nbr]:
                    DFS(nbr)
        print(adj)
        visited = [0 for i in range(n)]
        provinces = 0
        for i in range(n):
            if not visited[i]:
                DFS(i)
                print(visited)
                provinces+=1
        return provinces
