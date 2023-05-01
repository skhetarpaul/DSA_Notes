# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/submissions/936210681/
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.maxlen = 0
        @cache
        def DFS(node, moveLeft, pathlen):
            self.maxlen = max(self.maxlen, pathlen)
            if node is None:
                return
            else:
                #to go node.left
                DFS(node.left, False, pathlen+1) if moveLeft is True else DFS(node.left, False, 1)
                DFS(node.right, True, pathlen+1) if moveLeft is False else DFS(node.right, True, 1)

        DFS(root, True, 0)
        DFS(root, False, 0)
        return self.maxlen-1