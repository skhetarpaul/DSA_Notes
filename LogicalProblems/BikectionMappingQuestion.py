# https://leetcode.com/problems/word-pattern/description/

class Solution:



    def wordPattern(self, pattern, s):
        s = s.split()
        if len(s)!=len(pattern):
            return False
        dp = {}
        ds = {}
        for i in range(len(pattern)):
            p, st = pattern[i], s[i]
            if not p in dp and not st in ds:
                dp[p] = s[i]
                ds[st] = p
            elif p in dp and st in ds:
                if not (ds[st]==p or dp[p]==st):
                    return False
            else:
                return False
        return True