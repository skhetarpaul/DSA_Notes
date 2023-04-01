# https://leetcode.com/problems/longest-cycle-in-a-graph/description/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        adj = [[] for i in range(n)]
        visited = [0 for i in range(n)]
        ans = 0
        dfsVisited = [0 for i in range(n)]
        def checkDFS(node):
            visited[node] = 1
            dfsVisited[node] = 1
            for nbr in adj[node]:
                if visited[nbr]==0:
                    if checkDFS(nbr)==True:
                        return True
                elif visited[nbr]==1 and dfsVisited[nbr]==1:
                        return True
            dfsVisited[node] = 0
            return False

        for i, x in enumerate(edges):
            if x!=-1:
                adj[x].append(i)
        print(adj)
        for i in range(n):
            if not visited[i]:
                isCycle= checkDFS(i)
                # print(isCycle, i)
                if isCycle:
                    c= 1
                    start = i
                    while edges[start]!=i:
                        c+=1
                        start = edges[start]
                    ans = max(ans, c)
        return ans if ans > 0 else -1

