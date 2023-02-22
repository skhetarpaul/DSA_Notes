# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
'''Focus on finding a differentiator using Binary search, that in what case you cna tell whether thr element lkies in the left or element lies in the right.
That's all required for the question
'''

class Solution:
    def singleNonDuplicate(self, nums) -> int:
        low = 0
        high = len(nums)-1
        n = len(nums)
        while low<=high:
            mid = (low + high)//2
            leftelem = mid-low + 1
            if leftelem%2==0:
                #no of left elements is even, atleast one element at the left side
                if nums[mid-1]!=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                #no of left elements is odd, 0 or >0 elements at left
                if mid-1>=low and nums[mid-1]==nums[mid]:
                    high = mid-2
                elif mid-1>=low and nums[mid-1]!=nums[mid]:
                    low = mid
                else:
                    #mid-1 does not exists
                    high = mid-1
        return nums[low]