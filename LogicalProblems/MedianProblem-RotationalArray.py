# https://leetcode.com/problems/count-subarrays-with-median-k/description/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        index_k,n = -1, len(nums)
        for i in range(len(nums)):
            if nums[i]==k:
                index_k = i
                break
        d = defaultdict(int)
        current_sum = 0
        for x in range(index_k, n):
            if nums[x]>k:
                current_sum+=1
            elif nums[x]<k:
                current_sum-=1
                
            d[current_sum]+=1
        # print(d)
        #Till here I have made the dictionary items.
        result, current_sum = 0,0
        for x in range(index_k, -1,-1):
            if nums[x]>k:
                current_sum+=1
            elif nums[x]<k:
                current_sum-=1
            # print(current_sum)
            result+= d[-1*current_sum] + d[1-current_sum]
        return result
            