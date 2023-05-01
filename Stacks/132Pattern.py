# https://leetcode.com/problems/132-pattern/description/

'''A problem, not very intuitive O(n) sulution but attched is the answer.
Brute force:
O(n)^3 solution takes in the three loops, i, j, k and follow

O(n^2) approach, and O(n) approach
 :) cram this for now, maiontain a stack and previous minimum element. Stack elements should be in monotonically decreasing order.
 So if an element comes, and we know last minimum element
 This way we can track of an element i<j<k and arr[i]<arr[k]<arr[j]'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        mini = nums[0]
        for i in range(1, len(nums)):
            while not len(stk)==0 and stk[-1][0]<=nums[i]:
                # mini = min(stk[-1], mini)
                stk.pop()
            if len(stk)>=1 and nums[i]> stk[-1][1]:
                return True
            stk.append([nums[i], mini])
            mini = min(mini, nums[i])
        return False