# https://leetcode.com/problems/house-robber-iv/

'''Its good to always take an option to go thrpough a linear search if a value satisfies given set of conditions. 
This may be true if weneed tofind a maxima of minima or minima of maxima.
Then an optimization, could be to use Binary search as we used here.

If no idea, then possible hints could be:
    Length of array,
    Given are a set of conditions that can somehow be checked in o(n)
    Maxima of minimas or minima of maximas
    arr element could reach upto: 10**9'''

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def isPossible(x):
            count = 0
            last_steal_ind = float("-inf")
            for i in range(n):
                # print(last_steal_ind)
                if nums[i]>x or i == last_steal_ind + 1:
                    continue
                
                else:
                    last_steal_ind = i
                    count+=1
            # print(count, x, nums)
            return count>=k

        mini = 0
        maxi = 10**9+1
        while mini<maxi:
            mid = (maxi + mini)//2
            if isPossible(mid):
                maxi = mid
            else:
                mini = mid+1
        return mini