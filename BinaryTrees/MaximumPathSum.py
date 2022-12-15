'''Prerequisites:
Do Maximum height in a Binary tree,
Maximum width in  a Biary Tree'''
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxval = root.val
        self.solve(root)
        return self.maxval
    
    def solve(self, node):
        if node is None:
            return 0
        else:
            leftsum = max(0,self.solve(node.left))
            rightsum = max(self.solve(node.right),0)
            self.maxval = max(node.val + leftsum + rightsum, self.maxval)
            return node.val + max(leftsum, rightsum)
