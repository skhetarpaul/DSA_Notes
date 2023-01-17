class Solution:
    def rangeAddQueries(self, n: int, queries):
        aux = [[0 for i in range(n)] for j in range(n)]
        def updateQuery(x1, y1, x2, y2):
            aux[x1][y1]+=1
            if x2+1<n:
                aux[x2+1][y1]-=1
            if x2+1<n and y2+1<n:
                aux[x2+1][y2+1]+=1
            if y2+1<n:
                aux[x1][y2+1]-=1
        for X1,Y1,X2,Y2 in queries:
            updateQuery(X1,Y1,X2,Y2)
    
        for i in range(n):
            for j in range(1, n):
                aux[j][i]+=aux[j-1][i]
        for i in range(n):
            for j in range(1, n):
                aux[i][j]+=aux[i][j-1]


        return aux