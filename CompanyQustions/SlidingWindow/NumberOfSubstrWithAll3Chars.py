# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
'''Easy questio, just apply brains'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        i,j = 0,0
        num = 0
        docc = {}
        count = 0
        while j<n:
            c = s[j]
            if c in docc:
                docc[c]+=1
            else:
                count+=1
                docc[c] = 1
            if count==3:
                print(i,j)
                num+=n-j
            while count==3:
                docc[s[i]]-=1
                if docc[s[i]]==0:
                    docc.pop(s[i])
                    count-=1
                else:
                    num+=n-j
                i+=1
            j+=1
        return num
            