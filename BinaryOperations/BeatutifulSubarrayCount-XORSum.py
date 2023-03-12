# https://leetcode.com/contest/weekly-contest-336/problems/count-the-number-of-beautiful-subarrays/

'''In a nutshell, this problem simply asks you to find all subarrays whose XOR sum==0'''


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        prefixXor = [0 for i in range(len(nums)+1)]
        #this problem is equivalent to find the xor sum ==0
        n = len(nums)
        count = 0
        d = defaultdict(int)
        for i in range(n):
            prefixXor[i+1] = prefixXor[i]^nums[i]
            
        # print(prefixXor)
        for x in prefixXor:
            if d[x]>0:
                count+=d[x]
                d[x]+=1
            else:
                d[x] = 1
        return count
                
            
        
        