# https://leetcode.com/problems/contiguous-array/description/

#Most of Prefix sum problems utilize the concepts of dictionaary and calculating sum.
#Then you need to check whether same sum exists prevoiously, if yes then you can check max length.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {}
        currsum = 0
        hashmap[0] = -1
        res = 0
        for i in range(len(nums)):
            if nums[i]==0:
                currsum-=1
            else:
                currsum+=1
            if currsum in hashmap:
                res = max(res, i- hashmap[currsum])
            else:
                hashmap[currsum] = i
        return res
