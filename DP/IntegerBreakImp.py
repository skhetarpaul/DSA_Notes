# https://leetcode.com/problems/integer-break/description/

# Ca you think of an O(n) solution?

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def recursion(num):
            if num==1:
                return 1
            else:
                '''
                Below condition assures mandatory splitting 
                for base n and optionally allows a subdigit to 
                either remain the same or split further.
                '''
                maxi = 0 if num==n else num
                for i in range(1, num):
                    maxi = max(maxi, recursion(i)*recursion(num-i))
                return maxi
        def Tabulation():
            dp = [i for i in range(n+1)]
            for i in range(1, n+1):
                if i==1:
                    dp[i] = 1
                else:
                    half = i//2
                    for k in range(half, i):
                        print(k, i-k, dp[k], dp[i-k])
                        dp[i] = max(dp[i], dp[k]*dp[i-k])
            print(dp)
            return dp[-1]
        if n==1 or n==2:
            return 1
        elif n==3:
            return 2
        else:
            return Tabulation()
        # return recursion(n)