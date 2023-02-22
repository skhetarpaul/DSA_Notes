'''https://leetcode.com/problems/search-in-rotated-sorted-array/description/

This question checks the basic logic of Binary Search, using the logic here we can ask ourselves at any point of time, can we discard one half from ouyr search space?

At first, it looks bit tricky but try gather 2 scenarios, in any case our array is sorted so either our target lies in the left sorted part or right sorted part.

Look ponw carefully to understand the logic for the problem.'''

class Solution:
    def search(self, nums, target: int) -> int:
        #Certain whether the point is at left or at right
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low + high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[low]:
                if target<nums[mid] and target>=nums[low]:
                    high = mid-1
                else:
                    #target does not exists between low and mid
                    low = mid+1
            else:
                if target<=nums[high] and target>nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
        return -1