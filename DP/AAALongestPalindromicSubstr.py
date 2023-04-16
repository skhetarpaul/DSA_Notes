'''Should be one of the first probelms to consider in DP:
contains approach from Brute force to memoization to Tabulation and then finally Space optimizatiomn.
https://leetcode.com/problems/longest-palindromic-subsequence/description/
'''


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s2 = s[::-1]
        dp = {}
        def recursion(index1, index2):
            if index1==n or index2==n:
                return 0
            elif (index1, index2) in dp:
                return dp[(index1, index2)]
            
            else:
                if s[index1]==s2[index2]:
                    dp[(index1, index2)] = 1 + recursion(index1+1, index2+1)
                    return dp[(index1, index2)]
                else:
                    dp[(index1, index2)] = max(recursion(index1+1, index2), recursion(index1, index2+1))
                    return dp[(index1, index2)]


        def Tabulation():
            dp = [[0 for i in range(n+1)] for j in range(n+1)]
            for index1 in range(n,-1,-1):
                for index2 in range(n, -1,-1):
                    if index1==n or index2==n:
                        dp[index1][index2]==0
                    else:
                        if s[index1]==s2[index2]:
                            dp[index1][index2] = 1 + dp[index1+1][index2+1]
                        else:
                            dp[index1][index2] = max(dp[index1+1][index2], dp[index1][index2+1])
            return dp[0][0]
        # return Tabulation()
            
    
        def spaceOptimization(): 
            dp = [0 for i in range(n+1)]
            for index1 in range(n-1,-1,-1):
                curr = [0 for i in range(n+1)]
                for index2 in range(n-1, -1,-1):
                    if index1==n or index2==n:
                        curr[index2]=0
                    else:
                        if s[index1]==s2[index2]:
                            curr[index2] = 1 + dp[index2+1]
                        else:
                            curr[index2] = max(dp[index2], curr[index2+1])
                dp = curr
            return dp[0]



        return spaceOptimization()