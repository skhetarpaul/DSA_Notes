#Modified version of base problem: Number of subarrays with sum==k:
'''Here we will be required to solve this problem in the same fashion(makin dictionaries and checking if same item already exists in prefixsum dict.
The only modification needed here is to apply mod k operation in prefixsum array.
This will ensure unique entries from 1-k only and nothing else, hence we can simply use the dictionary'''
from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixmodArr = [i for i in nums]
        for i in range(1, len(nums)):
            prefixmodArr[i] = (prefixmodArr[i] + prefixmodArr[i-1])%k
        dprefixes = defaultdict(int)
        prefixmodArr[0]%=k
        print(prefixmodArr)
        count = 0
        for i in range(len(nums)):
            if prefixmodArr[i]==0:
                count+=1
            count+=dprefixes[prefixmodArr[i]]
            dprefixes[prefixmodArr[i]]+=1
        return count

        