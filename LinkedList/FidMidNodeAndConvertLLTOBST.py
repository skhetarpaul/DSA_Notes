# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
Learning: The best way to find the midnode in a linked list is to using 2 pointers, namely slow and fast.
Always initialize slow to head
fast to head.next.next
if fast reaches None or fast.next reaches None then slow.next has the element with the mid value'''
from typing import Optional


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        #It is intuitive to use a slow fast pointer technique to find mid element
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val, None, None)
        slow = head
        fast = head.next.next
        while fast is not None and fast.next is not None:
            slow= slow.next
            fast = fast.next.next
        midNode = TreeNode(slow.next.val, None, None)
        midNode.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        midNode.left = self.sortedListToBST(head)
        return midNode

