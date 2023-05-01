# https://leetcode.com/problems/maximal-rectangle/submissions/935657813/
'''A variation of MaximalRectangleHistogram
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def mah(row):
            # print("row is , ", row)
            nsr = [0]*len(row)
            nsl = [0]*len(row)
            stk = []
            #nsl
            for i in range(len(row)):
                while not len(stk)==0 and row[stk[-1]]>=row[i]:
                    stk.pop()
                if len(stk)==0:
                    nsl[i] = -1
                else:
                    nsl[i] = stk[-1]
                stk.append(i)
            
            stk = []
            for i in range(len(row)-1, -1, -1):
                while not len(stk)==0 and row[stk[-1]]>=row[i]:
                    stk.pop()
                if len(stk)==0:
                    nsr[i]=  len(row)
                else:
                    nsr[i] = stk[-1]
                stk.append(i)
                
            # print(nsl, nsr)
            for i in range(len(row)):
                nsr[i] = (nsr[i]-nsl[i]-1)*row[i]
            return max(nsr)
        # print(mah([6,2,5,4,5,1,6]))
        maxi = float("-inf")
        n = len(matrix)
        m = len(matrix[0])

        temp = [0 for i in range(m)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=="0":
                    temp[j]= 0
                else:
                    temp[j]+= int(matrix[i][j])
            # print("index to be considered", temp)
            possible = mah(temp)
            maxi = max(possible, maxi)
        return maxi