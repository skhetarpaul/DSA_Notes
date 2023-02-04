class Solution:
    def minCost(self, nums, k) -> int:
        n = len(nums)
        splitarr = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            sdict = defaultdict(int)
            splits = 0
            for j in range(i, n):
                sdict[nums[j]]+=1
                if sdict[nums[j]]==2:
                    splits+=2
                elif sdict[nums[j]]>2:
                    splits+=1
                splitarr[i][j] = splits
        # print(splitarr)
        def calcCost( start, end):
            # print(start, end, splitarr[start][end])
            return k + splitarr[start][end]
        @cache
        def recursion(index, start):
            if index==n:
                if start==n:
                    return 0
                else:
                    return calcCost(start, index-1)
            else:
                #case I, dont end here, continue
                casei = recursion(index+1, start)
                    
                #caseii: calculate trmmed cost till here
                trimmedcost = calcCost(start, index)
                # print(trimmedcost, start, index)
                caseii = trimmedcost + recursion(index+1, index+1)
    
                return min(casei, caseii)

        def Tabulation():
            dp = [[0 for i in range(n+1)] for j in range(n+1)]
            for index in range(n,-1,-1):
                for start in range(n,-1,-1):
                    if index==n and start==n:
                        dp[index][start]= 0
                    elif start==n or start>index:
                        dp[index][start]= 0
                    elif index==n:
                        dp[index][start] = calcCost(start, index-1)
                    else:
                        casei = dp[index+1][start]
                        caseii = calcCost(start, index) + dp[index+1][index+1]
                        dp[index][start] = min(casei, caseii)
            return dp[0][0]

        # return recursion(0, 0)
        return Tabulation()
                
                    