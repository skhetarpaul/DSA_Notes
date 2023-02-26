# https://leetcode.com/problems/get-equal-substrings-within-budget/description/

'''Intuition for Prefix sum/SLiding window would be application of substring where addition is required to match a condition i.e. to amtch <=maxcost'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [abs(ord(s[i])-ord(t[i])) for i in range(n)]
        print(diff)
        #Sliding window approach
        curr = 0
        res = 0
        i,j = 0,0
        while j<n:
            curr+=diff[j]

            if curr<=maxCost:
                res = max(res, j-i+1)
            else:
                while i<j and curr>maxCost:
                    curr-=diff[i]
                    i+=1
                if i==j:
                    #Check if curr>maxcost, if yes, incrememt i,j
                    if curr<=maxCost:
                        res = max(res, j-i+1)
            j+=1
        return res
