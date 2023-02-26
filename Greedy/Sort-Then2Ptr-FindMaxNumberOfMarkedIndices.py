'''How to think about this question:
So, the very first thing we need to do is sorting noting that we are never concerned about indices.

Next we can either apply a greedy binary search foran element in first half to an element in the right half.
Or an easier way, lets run a 2 ptr game.'''


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        i = 0
        ans = 0
        j = n//2 if n%2==0 else n//2+1
        while j<n:
            if 2*nums[i]<=nums[j]:
                i+=1
                j+=1
                ans+=2
            elif 2*nums[i]>nums[j]:
                j+=1
        return ans