# Divide Intervals Into Minimum Number of Groups
'''https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/'''
# Approach 1: Using Prefix sum
from heapq import heappop, heappush


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        maxval = 0
        for i in range(len(intervals)):
            maxval = max(maxval, intervals[i][1])
        prsum = [0]*(maxval+2)

        for i in range(len(intervals)):
            prsum[intervals[i][0]]+=1
            prsum[intervals[i][1]+1]-=1

        for i in range(1,len(prsum)):
            prsum[i]+=prsum[i-1]
        return max(prsum)


#Approach 2: Using Pririty Queue

class Solution:
    def minGroups(self, intervals) -> int:
        pq = []
        for left, right in sorted(intervals):
            if pq and pq[0] < left:
                heappop(pq)
            heappush(pq, right)
        return len(pq)
    
# Approach 3: Using Sweep Line
