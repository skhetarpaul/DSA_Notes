
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/description/
'''Problem is similar to ProbabilityMapping.py. The only differenc is here we need toi find a 2D number whose formula can be a little trickyto find.'''
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        totalarea = 0
        area = []
        self.rects = rects
        for rect in rects:
            a,b,x,y = rect
            area.append(abs((x-a+1)*(y-b+1)))
            totalarea+=area[-1]
        self.cursum = [0 for i in range(len(rects))]
        self.cursum[0] = area[0]
        for i in range(1,len(rects)):
            self.cursum[i] = self.cursum[i-1] + area[i]
        
        

    def pick(self) -> List[int]:
        def findUpperIndex(target, arr):
            low = 0
            high = len(arr)-1
            while high-low>1:
                mid = (low + high)//2
                if arr[mid]<=target:
                    low = mid + 1
                else:
                    high = mid
            if arr[low]>target:
                return low
            return high
        pick = random.randint(0, self.cursum[-1]-1)
        i = findUpperIndex(pick, self.cursum)
        xa, ya,xb,yb = self.rects[i]
        x = self.rects[i][0] + random.uniform(0, 1) * (self.rects[i][2] - self.rects[i][0] + 1) - 0.5
        y = self.rects[i][1] + random.uniform(0, 1) * (self.rects[i][3] - self.rects[i][1] + 1) - 0.5
        return [round(x), round(y)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()