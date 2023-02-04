# https://leetcode.com/problems/subarray-sum-equals-k/
from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        res = 0
        n = len(nums)
        dprefix = {}
        prefixsum = 0
        for i in range(n):
            prefixsum+=nums[i]
            if prefixsum==k:
                res+=1
            if prefixsum-k in dprefix:
                res+=dprefix[prefixsum-k]
            if prefixsum in dprefix:
                dprefix[prefixsum]+=1
            else:
                dprefix[prefixsum] = 1
        return res


# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/
class Solution:
    def numOfSubarrays(self, arr) -> int:
        count = 0
        subsum=0
        dprefix = defaultdict(int)
        for i in range(len(arr)):
            subsum+=arr[i]
            if subsum&1:
                count+=1
                count+=dprefix[2]
                dprefix[1]+=1
            else:
                count+=dprefix[1]
                dprefix[2]+=1
        return count%(10**9+7)
            