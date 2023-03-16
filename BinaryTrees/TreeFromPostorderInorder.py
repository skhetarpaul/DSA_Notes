# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idict = {}
        for i, x in enumerate(inorder):
            idict[x] = i
        
        def recursive(pstart, pend, istart, iend):
            if pstart>pend or istart> iend:
                return None
            else:
                node= TreeNode(postorder[pend], None, None)
                inorderpos = idict[postorder[pend]]
                numnodes = inorderpos-istart
                node.left = recursive(pstart,pstart +numnodes-1, istart, inorderpos-1)
                node.right = recursive(pstart + numnodes, pend-1, inorderpos+1,iend)
                return node
        return recursive(0, len(postorder)-1, 0, len(postorder)-1)

        
