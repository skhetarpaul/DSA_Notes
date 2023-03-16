'''https://leetcode.com/problems/check-completeness-of-a-binary-tree/editorial/'''


from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        def isValidOrder(order):
            for i in range(len(order)-1):
                if order[i]==-1 and order[i+1]>order[i]:
                    return False
            return True
        q = Queue()
        if not root:
            return True
        q.put(root)
        firstNoneNode = False
        while not q.empty():
            temp = q.get()
            if temp is None:
                if not firstNoneNode:
                    firstNoneNode = True
                else:
                    continue
            else:
                if firstNoneNode:
                    return False
                q.put(temp.left)
                q.put(temp.right)
        return True
                

            
