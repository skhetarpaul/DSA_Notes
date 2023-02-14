'''Count of fair pairs, iclude all pairs whose sum is in range[lower, upper].
Now, if we think intuituively, we can get a O(n2) algorithm we can deploy to solve the purpose.
Can we do better?

Note that, sorting wont affect as we only need two different indexes that lie in a range.
Once sorted, can we find a range of indexes which can satisfy our given conditions?
This is possible throuh Binary Search:
    lower limit, to find an index whose nums[index]>=lower
    upper limit, to find the index2 whose nims[index]<=upper
'''
# https://leetcode.com/contest/weekly-contest-332/problems/count-the-number-of-fair-pairs/
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        def lowerBound(arr, target):
            l = 0
            h = len(arr)-1
            while l<=h:
                mid = (l + h)//2
                if arr[mid]>=target:
                    h = mid-1
                else:
                    l = mid+1
            return l
        
        def upperBound(arr, target):
            l = 0
            h = len(arr)-1
            while l<=h:
                mid = (l + h)//2
                if arr[mid]<=target:
                    l = mid +1
                else:
                    h = mid-1
            return h
        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            lb = lower-nums[i]
            ub = upper-nums[i]
            li = lowerBound(nums, lb)
            ui = upperBound(nums, ub)
            if i>=li and i<=ui:
                ans+=ui-li
            else:
                ans+=ui-li+1
        return ans//2
            