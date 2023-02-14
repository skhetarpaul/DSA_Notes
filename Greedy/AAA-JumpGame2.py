#Includes a greedy and a DP approach of O(N) and O(N*N) resp.
# For more info, Greedy approach: https://www.youtube.com/watch?v=dJ7sWiOoK7g

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # @cache
        # def recursion(index):
        #     if index>=n-1:
        #         return 0
        #     mini = float("inf")
        #     for t in range(1, min(n, nums[index]+1)):
        #         mini = min(recursion(index + t) + 1, mini)
        #     return mini
        # return recursion(0)
        res = 0
        l = r = 0
        while r<n-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest
            res+=1
        return res
