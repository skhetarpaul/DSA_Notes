# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
'''In any of similar problems, wherer you need to minimize an operation for given range, TRY to sort the given array usually by endrange or arr[i][1]. 
Once sorted, keep pointer on first point and iterate, if range collides do nothing and continue.
If range does not collide, do increase counter(ans) by 1 and modify pointer to the current iteration's endpoint.'''
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
