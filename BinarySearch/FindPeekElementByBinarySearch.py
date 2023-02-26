# https://leetcode.com/problems/find-peak-element/description/
'''Intuition to use Binary Searc,
Question has asked to implement a o(logn) approach/algo for the problem
We might think that since the array is not sorted, how we can find the correct element in o(logn). But we need to see
that Biary search applies to all situations where we can decisively tell that there must be an element which we need to 
either side of the search space.
Say we go to the mid element, left element is greater but right element is smaller
    In this case, we can certainly tell that there exists atleast one peek element to the left(greater/greatest). Think about it
    
Similarly, we can consider for the right subarray as well'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low + high)//2
            if mid>0 and mid<n-1:
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return mid
                else:
                    if nums[mid]<nums[mid-1]:
                        high = mid-1
                    else:
                        low= mid+1
            elif mid==0:
                if n==1 or nums[mid+1]<nums[mid]:
                    return 0
                else:
                    low = mid+1
            else:
                #mid = n-1
                if n==1 or nums[mid-1]<nums[mid]:
                    return mid
                else:
                    high = mid-1
        return low
