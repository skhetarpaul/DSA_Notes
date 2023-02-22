# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        @cache
        def recursion(index, currxor):
            if index==len(nums):
                return currxor
            else:
                pick = recursion(index+1, currxor^nums[index])
                notpick = recursion(index+1, currxor)
                return pick + notpick
        return recursion(0, 0)
                
            