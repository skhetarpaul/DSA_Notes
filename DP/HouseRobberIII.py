# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def recursion(node):
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                return node.val
            else:
                profit = 0
                if node.left is not None and node.right is not None:
                    profit = max(profit, node.val + recursion(node.left.left) + recursion(node.left.right) + recursion(node.right.left) + recursion(node.right.right))
                elif node.left is not None:
                    profit = max(profit, node.val + recursion(node.left.left) + recursion(node.left.right))
                elif node.right is not None:
                    profit = max(profit, node.val + recursion(node.right.left) + recursion(node.right.right))
                profit = max(profit, recursion(node.left) + recursion(node.right))
                # profit = max(profit, recursion(node.right))
                return profit
        
        return recursion(root)

                