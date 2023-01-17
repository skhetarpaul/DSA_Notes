#Intuition for using Dijkstra algorithm:
'''Question is asking to find the SHORTEST path in the binary grid from a SINGLE source to a destination(SINGLE).
Why not visited?

Visited array makes no sense with Dijkstra algorithm as same node and edges can be covered more than once'''

import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # parent = [[-1 for i in range(n)] for j in range(n)]
        dist = [[float("inf") for i in range(n)] for j in range(n)]
        dist[0][0] = 0
        pq = []
        dirx = [-1,-1,0,1,1,1,0,-1]
        diry = [0,-1,-1,-1,0,1,1,1]
        def isValid(x,y):
            if x>=0 and x<n and y>=0 and y<n:
                return True
            return False
        heapq.heappush(pq, (0, (0,0)))
        if grid[0][0]==1:
            return -1
        while not len(pq)==0:
            distance, (x,y) = heapq.heappop(pq)
            # print(distance, x,y)
            for nbrx, nbry in zip(dirx, diry):
                nbrx = x + nbrx
                nbry = y+nbry
                if isValid(nbrx, nbry) and grid[nbrx][nbry]==0 and distance + 1<dist[nbrx][nbry]:
                    dist[nbrx][nbry] = distance + 1
                    heapq.heappush(pq, (distance + 1, (nbrx, nbry)))
        print(dist)
        return -1 if dist[n-1][n-1]==float("inf") else dist[n-1][n-1]+1
