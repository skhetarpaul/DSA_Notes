class Solution:
    def longestOnes(self, nums, k: int) -> int:
        i = 0
        count, maxc = 0, 0
        zeroes = 0
        n = len(nums)
        #handle k==0
        j = 0
        while j<n:
            if nums[j]==1:
                count+=1
                maxc = max(maxc, count)
            else:
                if zeroes<k:
                    count+=1
                    zeroes+=1
                    maxc = max(maxc, count)
                else:
                    #zeroes==k
                    #remove one previous zero and then add a new zero
                    while i<j and nums[i]!=0:
                        i+=1
                        count-=1
                    i+=1
                    maxc = max(maxc, count)
            j+=1
        return maxc

