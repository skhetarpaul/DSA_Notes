# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/901373316/



class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+ high)//2
            if nums[low]<=nums[mid]:
                #move to right if nums[high]<nums[mid]
                if nums[high]<nums[low]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                high = mid
        return nums[low]