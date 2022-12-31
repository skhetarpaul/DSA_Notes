#A simple logic of Backtracking works here.
# Try thinking in the way to count nodes as you move forward, if the count of nodes at end==count of emptynodes, then you are done.

class Solution:
    def uniquePathsIII(self, grid):
        emptycells = 0
        start = (-1,-1)
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    emptycells+=1
                elif grid[i][j]==1:
                    start = (i,j)
        visited = [[0 for i in range(m)] for j in range(n)]
        def isValid(x,y):
            if x>=0 and x<n and y>=0 and y<m and visited[x][y]==0 and grid[x][y]!=-1 and grid[x][y]!=1:
                #the grid  block is neither blocked or start point or already visited
                return True
            return False
        visited[start[0]][start[1]] = 1
        self.ans = 0
        def backtrack(x,y, count):
            if grid[x][y]==2: #end node
                # print("here")
                self.ans+=1 if count-1==emptycells else 0
                return
            else:
                directionx = [-1,1,0,0]
                directiony = [0,0,-1,1]
                for dx,dy in zip(directionx, directiony):
                    if isValid(x+dx,y+dy):
                        visited[x+dx][y+dy] = 1
                        backtrack(x+dx,y+dy,count+1)
                        visited[x+dx][y+dy] = 0
                return
        backtrack(start[0],start[1],0) 
        return self.ans