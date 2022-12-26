class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def recursion(index, bought):
            if index>=n:
                return 0
            else:
                if bought==-1:
                    #You have two choices, buy or not buy
                    buy = recursion(index+1, index)
                    notbuy = recursion(index+1, -1)
                    return max(buy, notbuy)
                else:
                    sell = prices[index]-prices[bought] + recursion(index+2,-1)
                    notsell = recursion(index+1, bought)
                    return max(sell, notsell)

        def Tabulation():
            dp = [[0 for bought in range(n+1)] for index in range(n+2)]
            for index in range(n+1,-1,-1):
                for bought in range(n,-1,-1):
                    if index>=n:
                        dp[index][bought] = 0
                    else:
                        if bought==0:
                            buy = dp[index+1][index+1]
                            notbuy = dp[index+1][0]
                            dp[index][bought] = max(buy, notbuy)
                        else:
                            sell = prices[index]-prices[bought-1] + dp[index+2][0]
                            notsell = dp[index+1][bought]
                            dp[index][bought] = max(sell, notsell)
            # print(dp)
            return dp[0][0]
        

        # return recursion(0,-1)
        return Tabulation()
