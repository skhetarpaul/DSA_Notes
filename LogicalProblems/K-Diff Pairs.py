

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        count = 0
        # visited = set()
        for key, val in sorted(d.items(), key = lambda x: x[0]):
            if val>0:
                d[key]-=1
                if key + k in d and d[key+k]>0:
                    count+=1
        return count
            