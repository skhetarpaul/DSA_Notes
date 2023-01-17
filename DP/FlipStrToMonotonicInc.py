
# https://leetcode.com/problems/flip-string-to-monotone-increasing/submissions/879754373/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = {}
        def recursion(index, mono):
            if index==n:
                return 0
            elif (index, mono) in dp:
                return dp[(index, mono)]
            else:
                if s[index]=='1' and mono:
                    #Currently I am encountering zeroes only and a 1 came
                    dp[(index, mono)] = min(1 + recursion(index+1, mono), recursion(index+1, False))
                elif s[index]=='0' and mono:
                    dp[(index, mono)] = min(1 + recursion(index+1, False), recursion(index+1, mono))

                elif not mono and s[index]=='0':
                    dp[(index, mono)] = 1 + recursion(index+1, mono)

                elif not mono and s[index]=='1':
                    dp[(index, mono)] = recursion(index+1, mono)

                return dp[(index, mono)] 
        return recursion(0, True)


# /////////////////////BEST APPROACH///////////////////////#
def minFlipsMonoIncr(self, s: str) -> int:
    countOnes = 0
    res = 0
    for i in s:
        if i=='1':
            countOnes+=1
        else:
            #i is '0'
            res = min(res+1, countOnes)
    return res