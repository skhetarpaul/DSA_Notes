# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        def findIfCycle(node):
            slow = node
            fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow==fast:
                    return slow
            return None
        
        intersectNode = findIfCycle(head)
        if intersectNode is None:
            return None
        else:
            start = head
            while start!=intersectNode:
                start = start.next
                intersectNode = intersectNode.next
            return start