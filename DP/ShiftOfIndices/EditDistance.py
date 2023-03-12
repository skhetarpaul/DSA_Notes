# https://leetcode.com/problems/edit-distance/description/

'''This question is a HARD category. Couple of things to note here, how to find if DP would be the correct approach?
You are asked to optimize the problem.
You can break the problem into smaller subproblem which is a prereq of DP
Constraints are small

Secondly, in Tabulation, how to shift the indices:
Note that in recursion we took if i<0 or j<0:
    Equivalence of above relation in Tabulation would be if i==0 or j==0 i.e. the string indices would be now 1 indexed.
    Hence logic changes a little bit.'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def recursion(i, j):
            if i<0 and j>=0:
                return j+1
            elif i>=0 and j<0:
                return i+1
            elif i<0 and j<0:
                return 0
            else:
                if word1[i]==word2[j]:
                    return recursion(i-1, j-1)
                else:
                    insert = 1 + recursion(i, j-1)
                    delete = 1 + recursion(i-1,j)
                    replace = 1 + recursion(i-1, j-1)
                    return min(insert, delete, replace)

        def Tabulation():
            dp = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
            for i in range(len(word2)+1):
                for j in range(len(word1)+1):
                    if i==0 and j>=1:
                        dp[i][j] = j
                    elif i>=1 and j==0:
                        dp[i][j] = i
                    elif i==0 and j==0:
                        dp[i][j] = 0
                    else:
                        # print(i, j)
                        if word2[i-1]==word1[j-1]:
                            dp[i][j] = dp[i-1][j-1]
                        else:
                            insert = dp[i][j-1]
                            delete = dp[i-1][j]
                            replace = dp[i-1][j-1]
                            dp[i][j] = 1 + min(insert, delete, replace)
            return dp[len(word2)][len(word1)]
        # return recursion(len(word1)-1, len(word2)-1)
        return Tabulation()

                