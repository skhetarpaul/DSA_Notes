# Longest Well Performing Interval
'''https://leetcode.com/problems/longest-well-performing-interval/description/

Note that slidin window approach cannot work here since we dont know how to manage i, j pointers in O(n). 
Further, consider a scenario -1,-1,-1,-1,-1,-1,1,1,1'''
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        psum = 0
        dsums = {}
        maxi = 0
        for i, h in enumerate(hours):
            if hours[i]>8:
                psum+=1
            else:
                psum-=1
            if psum>0:
                maxi = i+1
            else:
                if psum-1 in dsums:
                    maxi = max(maxi, i-dsums[psum-1])

            if psum not in dsums:
                dsums[psum] = i
        return maxi


