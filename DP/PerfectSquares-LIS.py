# https://leetcode.com/problems/perfect-squares/submissions/847980359/
# Clearly a DP Question:
# Includes 2 solutions, one in pattern of LIS and other one is plain DP recursion

import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            mini = float("inf")
            j = 1
            while j*j<=i:
                rem = i-j*j
                if dp[rem]<mini:
                    mini = dp[rem]
                j+=1
                dp[i] = mini + 1
        return dp[n]






'''
TLE SOLUTION
'''

import math
class Solution:
    def numSquares(self, n: int) -> int:
        def isPerfectSquare(x):
            srt = int(math.sqrt(x))
            if srt**2==x:
                return True
            return False
        @cache
        def recursion(i, target, used):
            if target==0:
                return used
            elif i>n:
                return float("inf")
            else:
                # print(i+1,target, used)
                notTaken = recursion(i+1,target, used)
                taken = float("inf")


                if target-i>=0 and isPerfectSquare(i):
                    # print("taken",i, target-i,used+1 )
                    taken = recursion(i, target-i,used+1)
                return min(taken, notTaken)
        if isPerfectSquare(n):
            return 1
        return recursion(1, n,0)