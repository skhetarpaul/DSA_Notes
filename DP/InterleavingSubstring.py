# https://leetcode.com/problems/interleaving-string/description/

'''
A typical DP problem, explained below is code for recursive, memoized and Tabulation for reference.
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2)!=len(s3):
            return False

        @cache
        def recursion(i,j):
            if i==len(s1):
                return s2[j:]==s3[i+j:]
            elif j==len(s2):
                return s1[i:]==s3[i+j:]
            else:
                #Take possibility of i
                possibility = False
                if s1[i]==s3[i+j]:
                    possible1 = recursion(i+1, j)
                    possibility = possible1 or possibility
                if s2[j]==s3[i+j]:
                    possible1 = recursion(i, j+1)
                    possibility = possible1 or possibility
                return possibility
        # dp = [[-1 for j in range(len(s2))] for i in range(len(s1))]
        def memoization(i,j):
            if i==len(s1):
                return s2[j:]==s3[i+j:]
            elif j==len(s2):
                return s1[i:]==s3[i+j:]
            elif dp[i][j]!=-1:
                return dp[i][j]
            else:
                possibility = False
                if s1[i]==s3[i+j]:
                    possible1 = memoization(i+1, j)
                    possibility = possible1 or possibility
                if s2[j]==s3[i+j]:
                    possible1 = memoization(i, j+1)
                    possibility = possible1 or possibility
                dp[i][j] = possibility
                return dp[i][j]

        def Tabulation():
            dp = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
            for i in range(len(s1),-1,-1):
                for j in range(len(s2),-1,-1):
                    if i==len(s1):
                        dp[i][j] = s2[j:]==s3[i+j:]
                    elif j==len(s2):
                        dp[i][j] = s1[i:]==s3[i+j:]
                    else:
                        possibility = False
                        if s1[i]==s3[i+j]:
                            possible = dp[i+1][j]
                            possibility = possibility or possible
                        if s2[j]==s3[i+j]:
                            possible = dp[i][j+1]
                            possibility = possibility or possible
                        dp[i][j] = possibility
            # print(dp)
            return dp[0][0]




        return Tabulation()
                    
