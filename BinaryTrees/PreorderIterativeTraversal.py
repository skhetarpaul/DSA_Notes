class Solution:
    def preorderTraversal(self, root):
        temp = root
        if root is None:
            return []
        ans = []
        stack = []
        stack.append(temp)
        print(stack)
        while len(stack)>0:
            topop = stack.pop()
            ans.append(topop.val)
            if topop.right is not None:
                stack.append(topop.right) 
            if topop.left is not None:
                stack.append(topop.left)
        return ans
            

# ========================================================


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return []
        stk = []
        stk.append(root)
        while len(stk)>0:
            temp = stk.pop()
            print(temp.val, temp.left, temp.right)
            if temp.left is not None:
                stk.append(temp.left)
            if temp.right is not None:
                stk.append(temp.right)
            ans.append(temp.val)
        return ans[::-1]
