# https://leetcode.com/problems/validate-stack-sequences/description/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = [pushed[0]]
        pushedc = 1
        poppedc = 0
        while True:
            while pushedc< len(pushed) and (len(stk)==0 or stk[-1]!= popped[poppedc]):
                stk.append(pushed[pushedc])
                pushedc+=1
            if stk[-1]==popped[poppedc]:
                stk.pop()
                poppedc+=1
                if poppedc==len(popped):
                    return True

            else:
                return False
        return True
