'''Simple solution:

U know that we use a stack here, right. Just iterate backward from the rightest element.
Stack maintained would be in the form increasing from top to bottom(highest element at the bottom of the stack)
# https://leetcode.com/problems/next-greater-element-ii/description/
'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk = []
        ans = [-1]*n
        for i in range(2*n-1, -1,-1):
            while len(stk)>0 and stk[-1]<=nums[i%n]:
                stk.pop()
            if i<n:
                if len(stk)==0:
                    ans[i] = -1
                else:
                    ans[i] = stk[-1]
            stk.append(nums[i%n])

        return ans
            