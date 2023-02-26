'''A simple question that involves a slightly tricky concept, say if you are at the start point
and next point distance is much away, in any case you wont be able to reach your destination.
But if you are intermediate stage, you still can get that point.
https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/'''


import heapq
class Solution:
    def minimumTime(self, grid) -> int:
        q = []
        m = len(grid)
        n = len(grid[0])
        def isValid(X,Y):
            if X>=0 and X<m and Y>=0 and Y<n:
                return True
            return False

        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        visited = [[0 for i in range(n)] for j in range(m)]
        heapq.heappush(q, (0,0,0)) #timer, tx, ty
        while not len(q)==0:
            timer, tx, ty = heapq.heappop(q)
            if (tx,ty)==(m-1,n-1):
                return timer
            else:
                dx = [-1,1,0,0]
                dy = [0,0,-1,1]
                for x, y in zip(dx, dy):
                    if isValid(x+tx,y+ty) and not visited[x+tx][y+ty]:
                        visited[x+tx][y+ty] = 1
                        if timer+1>=grid[x+tx][y+ty]:
                            heapq.heappush(q, (timer+1, x+tx, y+ty))
                        else:
                            if timer%2==0:
                                heapq.heappush(q, (grid[x+tx][y+ty]+1, x+tx, y+ty)) if grid[x+tx][y+ty]%2==0 else heapq.heappush(q, (grid[x+tx][y+ty], x+tx, y+ty))
                            else:
                                heapq.heappush(q, (grid[x+tx][y+ty], x+tx, y+ty)) if grid[x+tx][y+ty]%2==0 else heapq.heappush(q, (grid[x+tx][y+ty]+1, x+tx, y+ty))

        return -1
