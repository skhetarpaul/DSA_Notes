# https://www.codingninjas.com/codestudio/problems/paint-house_1460385?leftPanelTab=1


def minCost(cost):
    n = len(cost)
    def solve(dp, house, prev):
        if house==n:
            return 0
        elif dp[house][prev]!=-1:
            return dp[house][prev]
        else:
            mini = float("inf")
            for i in range(3):
                if i!=prev:
                    mini = min(mini, cost[house][i] + solve(dp,house+1, i))
            dp[house][prev] = mini
            return mini
        
    def Tabulation():
        dp = [[0 for i in range(3)] for j in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(3):
                if i==n-1:
                    dp[i][j] = cost[i][j]
                else:
                    mini = float("inf")
                    for k in range(3):
                        if k!=j:
                            mini = min(mini, cost[i][j] + dp[i+1][k])
                    dp[i][j] = mini
        return min(dp[0])
                            
#     dp = [[-1 for i in range(4)] for j in range(n)]
#     return solve(dp,0,3)
    return Tabulation()