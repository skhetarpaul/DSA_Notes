import bisect
class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        if minK not in nums or maxK not in nums:
            return 0
        else:
            minI = -1
            maxI = -1
            start = 0
            count = 0
            for i in range(len(nums)):
                if nums[i]<minK or nums[i]>maxK:
                    start = i+1
                    minI, maxI = -1,-1
                else:
                    if nums[i]==minK:
                        minI = i
                    if nums[i]==maxK:
                        maxI = i
                    if minI!=-1 and maxI!=-1:
                        count+=min(minI, maxI) - start+1
            return count
                
            
