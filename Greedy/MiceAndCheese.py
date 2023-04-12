# https://leetcode.com/problems/mice-and-cheese/

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        
        diff = []
        for i, x in enumerate(reward1):
            diff.append((i, x-reward2[i]))
        diff = sorted(diff, key = lambda x: x[1], reverse = True)
        ans = 0
        for i in range(len(diff)):
            if k>0:
                ans+=reward1[diff[i][0]]
                k-=1
            else:
                ans+=reward2[diff[i][0]]
        return ans
            
            
#         def Tabulation():
#             dp = [[0 for i in range(k)] for j in range(n+1)]
#             for index in range(n,-1,-1):
#                 for k in range(min(index, k),-1,-1):
                
            