# https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        shiftI = [0]*(len(s)+2)
        n = len(s)
        for fi, ti, d in shifts:
            if d==0:
                d = -1
            shiftI[ti+1]+=d
            shiftI[fi]-=d
        print(shiftI)
        for i in range(n,0,-1):
            shiftI[i] = shiftI[i+1] + shiftI[i]
        def shiftCharacter(c, d):
            si = (ord(c)-97 + d%26)%26
            return chr(si + 97)
        news  = ''
        for index,c in enumerate(s):
            newc = shiftCharacter(c, shiftI[index+1])
            news+=newc
        return news
