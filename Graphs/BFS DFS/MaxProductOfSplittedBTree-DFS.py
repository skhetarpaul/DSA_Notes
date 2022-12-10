# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/
'''
Question just asks to break an edge in the Binary Tree such that tree 
is divided into 2 subtrees. Find maximized value of product of sum of 
these two subtrees.
Just use  the Brute Force/DFS method to run through the algorithm.
'''
from queue import Queue

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        totalSum = 0
        if root is None:
            return 0
        q = Queue()
        q.put(root)
        while not q.empty():
            temp = q.get()
            totalSum+=temp.val
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)
        print(totalSum)
        # return 3
        self.maxProduct = 0
        def treeSum(node):
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                self.maxProduct = max(self.maxProduct, node.val*(totalSum-node.val))
                return node.val
            else:
                leftsum = treeSum(node.left)
                rightsum = treeSum(node.right)
                self.maxProduct = max(max(self.maxProduct, leftsum*(totalSum-leftsum)), rightsum*(totalSum-rightsum))
                # return self.maxProduct
                return leftsum + rightsum + node.val
        treeSum(root)
        return self.maxProduct%(10**9+7)

