# https://leetcode.com/problems/car-pooling/solutions/

import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dest = []
        trips = sorted(trips, key = lambda x: x[1]) #sort by from value
        # print(trips)
        heapq.heappush(dest, (trips[0][2],0))
        people = trips[0][0]
        if people>capacity:
            return False
        i = 1
        n = len(trips)
        while i<n:
            while len(dest)>0 and dest[0][0]<=trips[i][1]:
                #until destination is of len==0 or destination<next start point
                d, index = heapq.heappop(dest)
                people-=trips[index][0]
            if people + trips[i][0]<=capacity:
                people+= trips[i][0]
                heapq.heappush(dest, (trips[i][2], i))
            else:
                return False
            i+=1
        return True