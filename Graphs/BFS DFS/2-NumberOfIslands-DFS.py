class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        count = 0
        def isValid(a,b):
            if a>=0 and b>=0 and a<m and b<n:
                return True
            return False

        def DFS(x, y):
            visited[x][y] = 1
            dx = [1,0, -1,0]
            dy = [0,1, 0,-1]
            for i, j in zip(dx, dy):
                if isValid(i + x, j + y) and visited[i+x][j+y]==0 and grid[i+x][j+y]=='1':
                    DFS(i+x, j+y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]==0:
                    count+=1
                    DFS(i,j)
        return count