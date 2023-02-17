# https://leetcode.com/problems/increment-submatrices-by-one/

'''This problem cn be solved using Prefix sum approach, say you are given (x1,y1) (x2,y2)

1 2 3 4 2 1
1 0 0 9 8 6
2 3 4 5 2 2
0 0 0 1 1 1
 Say you have this matrix above and you need to inc 1 in submat from (1,1)-> (3,2)
 Prefix sum approach says,
 Add 1 to (x1, y1)
 Subtract 1 from (x1,y2+1)
 subtract 1 from (x2+1, y1)
 Add 1 to (x2+1, y2+1)
 '''

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
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