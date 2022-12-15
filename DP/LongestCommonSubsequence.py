class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        @cache
        def recursion(i, j):
            if i<0 or j<0:
                return 0
            else:
                if text1[i]==text2[j]:
                    return 1 + recursion(i-1,j-1)
                else:
                    return max(recursion(i-1,j), recursion(i,j-1))

        def Tabulation():
            dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
            for i in range(n1+1):
                for j in range(n2+1):
                    if i==0 or j==0:
                        dp[i][j] = 0
                    else:
                        if text1[i-1]==text2[j-1]:
                            dp[i][j] = 1 + dp[i-1][j-1]
                        else:
                            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[n1][n2]
        return Tabulation()
