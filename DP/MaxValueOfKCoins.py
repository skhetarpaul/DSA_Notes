# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/solutions/?orderBy=hot

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        def getPrefixSum(arr):
            prsum = {0: 0}
            for i in range(len(arr)):
                prsum[i+1] = prsum[i]+arr[i]
            print(prsum)
            return prsum
        pilesdict = [{} for i in range(n)]
        for i, x in enumerate(piles):
            pr = getPrefixSum(x)
            pilesdict[i] = pr
        @cache
        def recursion(index, k):
            if k==0:
               return 0 
            elif index==n:
                if k==0:
                    return 0
                else:
                    return float("-inf")
            else:
                maxival = 0
                for key, val in pilesdict[index].items():
                    if key<=k:
                        pick = val + recursion(index+1, k-key)
                        maxival = max(pick, maxival)
                    else:
                        break
                # notpick = recursion(index+1, k)
                # maxival = max(maxival, notpick)
                return maxival

        return recursion(0, k)
        