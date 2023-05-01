
# https://leetcode.com/problems/trapping-rain-water/description/
'''Typical question: Note that thisquestion has a pattern, though it soes not relates with nearest greater/smaller element at either side. Still, you can easily find the level of water above the array using the maximum value at either side (left and right subarray)
https://www.youtube.com/watch?v=FbGG2qpNp4U&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=9
'''

class Solution:
    def trap(self, heights: List[int]) -> int:
        mxl = [0]*len(heights)
        mxr = [0]*len(heights)
        mxl[0] = heights[0]
        for i in range(1, len(heights)):
            mxl[i] = max(mxl[i-1], heights[i])
    
        mxr[len(heights)-1] = heights[len(heights)-1]
        for i in range(len(heights)-2, -1, -1):
            mxr[i] = max(mxr[i+1], heights[i])

        for i in range(len(heights)):
            mxl[i] = min(mxl[i], mxr[i])
        totalwater = 0
        for i in range(len(heights)):
            totalwater += mxl[i]-heights[i]
        return totalwater