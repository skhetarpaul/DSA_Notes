# https://leetcode.com/problems/next-permutation/description/
# https://leetcode.com/problems/next-greater-element-iii/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        #3 important algorithmic observations:
        #1: Find a breakpoint, where arr[i]<arr[i+1]
        i = n-2
        index = -1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index = i
                break
        if index==-1:
            print("edgecase")
            #we simply reverse the array as the answer would be the first permutation itself
            nums.reverse()
        else:
            #2:find just greater element than the nums[index] which is not covered
            for i in range(n-1,index,-1):
                if nums[i]>nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break
            #3: Simply reverrse the array in place for the remaining elements

            nums[index+1:] = nums[index+1:][::-1]

