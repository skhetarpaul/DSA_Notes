# https://www.youtube.com/watch?v=-h_1GySuH2k
# A very important question, utilizing Prefix sum and VBinary search together
'''
Binary search: It can be applied whereever we can make a certain decision whether to move left or right.'''

class Solution:

    def findRightIndex(self,req, prefix, l,r, n):
        while l<r:
            m = (l+r)//2
            isPossible = True
            for ch in range(3):
                
                if prefix[ch][n]-prefix[ch][m]<req[ch]:
                    isPossible = False
                    break
            if isPossible:
                l = m+1
            else:
                r = m
        return l
            
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        mini = n
        prefix = [[0 for i in range(n+2)] for j in range(3)]
        for i in range(1,n+1):
            for j in range(3):
                prefix[j][i] = prefix[j][i-1] + 1 if j==ord(s[i-1])-ord('a') else prefix[j][i-1]
        for i in range(3):
            prefix[i][n+1] = prefix[i][n]
        if k==0:
            return 0
        elif prefix[0][n]<k or prefix[1][n]<k or prefix[2][n]<k:
            return -1
        for l in range(0,n):
            req = [max(0,k-prefix[i][l]) for i in range(3)]
            min_r = self.findRightIndex(req, prefix ,l+1,n+1,n+1)
            mini = min(mini, l+n+1-min_r)
        return mini
            


        
                