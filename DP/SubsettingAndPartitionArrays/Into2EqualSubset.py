class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        halfsum = totalsum//2
        if halfsum*2!=totalsum:
            return False
        else:
            n = len(nums)
            # @cache
            def recursion(index, target):
                if target==0:
                    return True
                elif index==n and target>0:
                    return False
                else:
                    notpick = recursion(index+1, target)
                    pick = False
                    if nums[index]<=target:
                        pick = recursion(index+1, target-nums[index])
                    return pick or notpick
            # return recursion(0, halfsum)

            def Tabulation():
                dp = [[0 for i in range(n+1)] for j in range(halfsum+1)]
                for target in range(0,halfsum+1,1):
                    for index in range(n-1,-1,-1):
                        if target==0:
                            dp[target][index] = True
                        elif index==n-1:
                            dp[target][index] = False
                        else:
                            notpick = dp[target][index+1] if index<n-1 else False
                            pick = dp[target-nums[index]][index+1] if target>=nums[index] else False
                            
                            dp[target][index] = pick or notpick
                # print(dp)
                return dp[halfsum][0]
            
            return Tabulation()

                            

