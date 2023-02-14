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
