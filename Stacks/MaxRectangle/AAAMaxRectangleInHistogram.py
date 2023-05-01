# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
'''A simple variation ofNext smaller element to right and next smaller element to right'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nsr = [0 for i in range(n)]
        nsl = [0 for i in range(n)]

        stk = []
        #for nsl
        for i in range(n):
            while not len(stk)==0 and heights[stk[-1]]>=heights[i]:
                stk.pop()
            if len(stk)==0:
                nsl[i] = -1
            else:
                nsl[i] = stk[-1]
            stk.append(i)
        print(nsl)
        stk = []

        for i in range(n-1, -1, -1):
            while not len(stk)==0 and heights[stk[-1]]>=heights[i]:
                stk.pop()
            if len(stk)==0:
                nsr[i] = n
            else:
                nsr[i] = stk[-1]
            stk.append(i)
        print(nsr)
        for i in range(n):
            nsr[i] =( nsr[i]-nsl[i]-1)*heights[i]
        return max(nsr)