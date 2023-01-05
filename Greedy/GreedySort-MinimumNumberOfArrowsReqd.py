# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

class Solution:
    def findMinArrowShots(self, points):
        if points==[]:
            return 0
        points = sorted(points, key = lambda x: x[1])
        
        ans=1
        n = len(points)
        currshot = points[0][1]
        for i in range(1,n):
            if points[i][0]<=currshot:
                continue
            else:
                ans+=1
                currshot = points[i][1]
        return ans
