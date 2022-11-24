# https://leetcode.com/problems/01-matrix/submissions/849099524/

from queue import Queue
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q= Queue()
        n = len(mat)
        m = len(mat[0])
        ans = [[float("inf") for i in range(m)] for j in range(n)]
        visited = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.put((i,j,0))
                    visited[i][j] = 1
        def isValid(a,b):
            if a>=0 and a<n and b>=0 and b<m and visited[a][b]==0:
                return True
            return False
        while not q.empty():
            tx,ty,d = q.get()
            ans[tx][ty] = d
            nbrx = [-1,1,0,0]
            nbry = [0,0,-1,1]
            for dx,dy in zip(nbrx,nbry):
                if isValid(dx+tx,dy+ty):
                    q.put((dx+tx,dy+ty,d+1))
                    visited[dx+tx][dy+ty] = 1
        return ans

