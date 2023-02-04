'''Learning: 
Hard question might not be as tough as they seem to be
Given time complexity 100000 (10**5)-> It is a high probablility either Binary search PQueue or sorting works here.

You need not the entire array, only the first and last values, hence you can break down the array ny splitting the vals'''


from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        mini= maxi = weights[0] + weights[n-1]
        if k==1 or n==1:
            return 0

        vals = []
        for i in range(n-1):
            vals.append(weights[i] + weights[i+1])
        vals.sort()
        v = len(vals)
        for i in range(k-1):
            mini+=vals[i]
            maxi+=vals[v-1-i]
        return maxi-mini

