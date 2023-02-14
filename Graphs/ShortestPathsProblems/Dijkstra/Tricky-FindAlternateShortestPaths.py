# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
'''Note the slight change in question hence change in answer.'''


import heapq

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        pq = []
        adj = [set() for i in range(n)]
        for a,b in redEdges:
            
            adj[a].add((b, 1))
        for u,v in blueEdges:
            
            adj[u].add((v, 0))
        # print(adj)
        distance = [float("inf") for i in range(n)]
        distance[0] = 0
        visited = set()
        visited.add((0,True))
        visited.add((0,False))
        heapq.heappush(pq, (0,0,True))
        heapq.heappush(pq, (0,0,False))
        while not len(pq)==0:
            dist,node, color = heapq.heappop(pq)
            # print(node, dist, color, "popped")
            # print(pq)
            for nbr, ncolor in adj[node]:
                # print(nbr, ncolor)
                if ncolor!=color:
                    # print("I entered inside")
                    if distance[nbr]>dist + 1:
                        distance[nbr] = dist + 1
                    # print(visited)
                    if (nbr, ncolor) not in visited:
                        # print(nbr, ncolor, "not in visited")
                        visited.add((nbr, ncolor))
                        heapq.heappush(pq,(dist + 1,nbr, not color))
        for i in range(n):
            if distance[i]==float("inf"):
                distance[i] = -1
        return distance