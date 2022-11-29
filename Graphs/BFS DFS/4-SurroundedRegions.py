# https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        visited = set()

        def isValid(i,j):
            if i>=0 and i<m and j>=0 and j<n and board[i][j]=="O":
                return True
            return False

        def DFS(x, y):
            nbrx = [-1,1,0,0]
            nbry = [0,0,-1,1]
            for nx,ny in zip(nbrx,nbry):
                if isValid(x+nx,y+ny) and (x+nx,y+ny) not in visited:
                    visited.add((x+nx,y+ny))
                    board[x+nx][y+ny] = "P"
                    DFS(x+nx,y+ny)
        
        for i in range(m):
            for j in range(n):
                if ((i==0 or i==m-1) or (j==0 or j==n-1)) and board[i][j]=="O" and (i,j) not in visited:
                    # print(i,j)
                    #This checks only corner edges are covered
                    board[i][j] = "P"
                    visited.add((i,j))
                    DFS(i,j)
        # print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j] = "X"
                elif board[i][j]=="P":
                    board[i][j] = "O"

        

        
