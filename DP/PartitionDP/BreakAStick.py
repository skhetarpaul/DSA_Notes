# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def recursion(i, j):
            if j-i==1:
                return 0
            else:
                mini = float("inf")
                presentf = 0
                for cut in cuts:
                    
                    if cut>i and cut<j:
                        presentf = 1
                        possible = j-i + recursion(i, cut) + recursion(cut, j)
                        mini = min(possible, mini)
                if presentf==0:
                    return 0
                return mini
        return recursion(0, n)