# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''Note that the Brute force approach, might not work here as it almost has n^3 complexity.
Can we think of a better approach? We can convert the subtree into a string.

This coul;d be a very important methodology to compare two subtrees.
'''
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        subtrees = defaultdict(int)
        def preorder(node):
            if node is None:
                return 'null'
            s = ",".join([str(node.val), preorder(node.left), preorder(node.right)])
            if subtrees[s]==1:
                ans.append(node)
            subtrees[s]+=1
            return s
        preorder(root)
        return ans
            


            
        
            
                
