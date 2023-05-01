'''One kind of questio, where we can explore the limits and playarounds. Check the problem, 
it is clearly mentioned that nums[i]>=-50 and nums[i]<=50.
Hence to find xth negative interger, wouldnt it  be simpler to count frequency of each negative number in a subarray
and then iterate through all 50 negative numbers to see, whose frewuency matches.

https://leetcode.com/problems/sliding-subarray-beauty/description/
'''

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        counter = [0]*51
        n = len(nums)
        i, j = 0, 0
        ans = []
        while j<n:
            if nums[j]<0:
                counter[nums[j]+50]+=1
            if j-i+1<k:
                pass
            else:
                count = 0
                c = -1
                while c<50 and count<x:
                    c+=1
                    count+=counter[c]
                if c<50:
                    ans.append(c-50)
                else:
                    ans.append(0)

                if nums[i]<0:
                    counter[nums[i]+50]-=1
                i+=1
            j+=1
        return ans