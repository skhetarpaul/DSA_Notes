#Intuition: We need to figure out different numbers, but we cannot chose.
# So create a heapq and iteratively save the numbers after multiplication from 2,3,5
# Use a disctionary to avoid duplicates as (3*2)==(2*3) = 6
# https://leetcode.com/problems/ugly-number-ii/description/


import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        d = {}
        q = []
        heapq.heappush(q,1)
        d[1] = 1
        k = 0
        while k<n:
            popped = heapq.heappop(q)
            print(popped, k)
            k+=1
            if k==n:
                return popped
            else:
                if popped*2 not in d:
                    heapq.heappush(q, popped*2)
                    d[popped*2] = 1
                if popped*3 not in d:
                    heapq.heappush(q, popped*3)
                    d[popped*3] = 1
                if popped*5 not in d:
                    heapq.heappush(q, popped*5)
                    d[popped*5] = 1
                