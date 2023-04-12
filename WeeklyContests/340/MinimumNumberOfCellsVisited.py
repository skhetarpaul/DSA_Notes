# Refer to all submitted solution, you will find out that somehow each represents some of the brute force approaches:
# Naive 1: Simple BFS-> Minimum is asked
# Naive 2: Simple recursiove solution and its optimization using cache/memoization
# Naive 3: Uding PQueue or dijkstra algoritjhm.

# https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/description/
from queue import Queue
import heapq

class Solution:
    
        
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pq = []
        distance = [[float("inf") for i in range(n)] for j in range(m)]

        distance[0][0] = 1
        def isValid(x, y):
            if x>=0 and x<m and y>=0 and y<n:
                return True
            return False
            
        heapq.heappush(pq, (1, (0,0)))
        while not len(pq)==0:
            cells, cord = heapq.heappop(pq)
            i, j = cord[0], cord[1]
            if i== m-1 and j==n-1:
                return cells
            else:
                for k in range(j+1, grid[i][j] + j+ 1):

                    if isValid(i, k) and distance[i][k]> cells+1:
                        distance[i][k] = cells+1
                        heapq.heappush(pq, (cells+1, (i, k)))
                        if i== m-1 and k==n-1:
                            return cells+1
                for k in range(i+1, grid[i][j] + i+1):
                    if isValid(k,j) and distance[k][j] >cells+1:
                        distance[k][j] = distance[i][j]+1
                        heapq.heappush(pq, (cells+1, (k, j)))
                        if k== m-1 and j==n-1:
                            return cells+1
        return -1

                