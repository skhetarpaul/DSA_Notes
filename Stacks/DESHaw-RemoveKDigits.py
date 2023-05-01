'''The base idea of the tack impelemtation would be to put things in increasing order from left to right.'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for i in range(len(num)):
            while len(stk)>0 and stk[-1]>num[i] and k>0:
                stk.pop()
                k-=1
            stk.append(num[i])
        
        while k>0:
            stk.pop()
            k-=1
        
        return str(int(''.join(stk))) if len(stk)>0 else "0"

            