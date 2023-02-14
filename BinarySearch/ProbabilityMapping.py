import random
import bisect
class Solution:

    def __init__(self, w):
        self.n = len(w)
        self.cursum = [0 for i in range(len(w))]
        self.cursum[0] = w[0]
        for i in range(1, self.n):
            self.cursum[i] = self.cursum[i-1] + w[i]

    def pickIndex(self) -> int:
        def findNextUpper(target, arr):
            beg, end = 0, len(arr)-1
            while end-beg>1:
                mid = (beg + end)//2
                if arr[mid]<=target:
                    beg = mid+1
                elif arr[mid]>target:
                    end = mid
            
            if arr[beg]>target:
                return beg
            if arr[end]>target:
                return end
            
        res = []
        rand = random.randint(0, self.cursum[-1]-1)
        # return bisect.bisect_right(self.cursum, rand)
        temp = findNextUpper(rand, self.cursum)
        return temp
        




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()