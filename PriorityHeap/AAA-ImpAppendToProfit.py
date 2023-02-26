# https://leetcode.com/problems/ipo/description/
# https://www.youtube.com/watch?v=Q5K6vRDs2k4

import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pq = []
        combined = sorted(zip(capital, profits), key = lambda x:( x[0]))
        # print(combined)
        maxp = w
        q = 0
        i = 0
        while i<len(combined) and q<k:
            while i<len(combined) and maxp>=combined[i][0] and q<k:
                heapq.heappush(pq, -1*combined[i][1])
                i+=1
            if len(pq)>0:
                wealth = -1*heapq.heappop(pq)
                maxp+=wealth
                q+=1
                # print(maxp, "current")
            else:
                return maxp

            
        while len(pq)>0 and q<k:
            # print("got here")
            maxp+=-1*heapq.heappop(pq)
            q+=1

        return maxp


        
            