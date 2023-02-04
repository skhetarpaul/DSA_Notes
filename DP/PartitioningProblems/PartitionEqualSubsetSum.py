class Solution:
    def spaceOptimized(self, n, k, dp, arr):
        for i in range(n):
            temp = [0 for i in range(k+1)]
            for t in range(k+1):
                if t==0:
                    temp[t] = True
                elif i==0 and t==arr[0]:
                    temp[t] = True
                else:
                    take = False
                    if arr[i]<=t:
                        take = dp[t-arr[i]]
                    notTake = dp[t]
                    temp[t] = take or notTake
            dp = temp
        return dp[-1]
    def canPartition(self, nums: List[int]) -> bool:
        arrSum = 0
        for i in nums:
            arrSum+=i
        if arrSum%2!=0:
            return False
        k = arrSum//2
        n = len(nums)
        dp = [0 for i in range(k+1)]
        return self.spaceOptimized(n,k, dp, nums)