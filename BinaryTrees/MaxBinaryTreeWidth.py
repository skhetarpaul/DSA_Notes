# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''A peculiar question of its type: The brute force of attaching None nodes and count 
    the no. of nodes doesnot works here.

The intuition behind the API is:
    Index every node at the index say node i(children will have index 2*i+1, 2*i+2)
    And at each level, capture first and last node index and last-first+1 is used for answer.
    Furthermore, since index is doubled everytime, hence there could be a need to avoid overflow:
    We subtract a minindex-> given in line 29.(TODO) from every node index and then assign 2*i+1, 2*i+2
'''
from queue import Queue

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = Queue()
        if root is None:
            return 0
        else:
            ans = 0
            q = Queue()
            q.put((root, 0))
            while not q.empty():
                first, last = None, None
                s = q.qsize()
                minindex = q.queue[0][1]
                for i in range(s):
                    temp, currw = q.get()
                    currid = currw - minindex
                    if i==0:
                        first = currid
                    if i==s-1:
                        last = currid
                    if temp.left:
                        q.put((temp.left, currid*2+1))
                    if temp.right:
                        q.put((temp.right, currid*2+2))
                ans = max(ans, last-first+1)
            return ans
                        
