# https://leetcode.com/problems/minimize-maximum-of-array/description/
'''This problem can be done through multiple approaches but the most intuitive one is ehre.
You need to note that, the pattern is minimizing the maximum. This gives a hint to use Binary search or an iterative search.
Further, if you can reduce an array value to minimum maximum, you have the answer. Hence the algo works'''

import copy

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        minval = min(nums)
        maxval = max(nums)
        def isPossible(mid, arr):
            temp = arr
            n = len(arr)
            
            for i in range(n-1,0,-1):
                if arr[i]>mid:
                    arr[i-1]+=arr[i]-mid
            arr = temp
            return arr[0]<=mid

        temp = nums
        while minval<=maxval:
            
            mid = (minval + maxval)//2
            # print(minval, maxval, mid)
            if isPossible(mid, copy.deepcopy(nums)):
                
                maxval = mid-1
            else:
                minval = mid+1
        return minval
