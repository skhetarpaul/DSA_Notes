import operator

# https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/856126472/
'''Might be confusing to understand, refer to the videos for understanding.
'''
class Solution:
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        def recursion(s):
            if s.isdigit():
                return [int(s)]
            else:
                res = []
                for i in range((len(s))):
                    if s[i] in "+-*":
                        nums1 = recursion(s[:i])
                        nums2 = recursion(s[i+1:])
                        # res+= [ops[s[i]](nums1, nums2) for num1 in nums1 for num2 in nums2]
                        res += [ops[s[i]](num1, num2) for num1 in nums1 for num2 in nums2]
                return res
    
        return recursion(expression)