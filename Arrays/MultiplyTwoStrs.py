
# https://leetcode.com/problems/multiply-strings/submissions/925262810/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return '0'
        num1 = [int(x) for x in num1]
        num2 = [int(y) for y in num2]
        num1 = num1[::-1]
        num2 = num2[::-1]

        ans = [0 for i in range(len(num1) + len(num2))]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                ans[i1+i2]+=num1[i1]*num2[i2]
                ans[i1+i2+1] += ans[i1+i2]//10
                ans[i1+i2]=ans[i1+i2]%10
        print(ans)
        res = ans[::-1]
        beg = 0
        while beg<len(res) and res[beg]==0:
            beg+=1
        return "".join(str(x) for x in res[beg:])

