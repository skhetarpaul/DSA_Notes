class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        combined = sorted(zip(rocks, capacity), key = lambda x: (x[1]-x[0],x[0]) )
        ans = 0
        for rock,cap in combined:
            if rock==cap:
                ans+=1
            elif additionalRocks>=(cap-rock):
                additionalRocks-=(cap-rock)
                ans+=1
            else:
                return ans
        return ans