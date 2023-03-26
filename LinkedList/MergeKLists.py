# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(left, right):
            dummy = ListNode()
            temp = dummy
            while left is not None and right is not None:
                if left.val<right.val:
                    temp.next = ListNode(left.val)
                    temp = temp.next
                    left = left.next
                else:
                    temp.next = ListNode(right.val)
                    temp = temp.next
                    right = right.next
            if left is not None:
                temp.next = left
            if right is not None:
                temp.next = right
            return dummy.next



        def mergeSort(lists, start, end):
            if start>end:
                return None
            elif start==end:
                return lists[start]
            else:
                mid = (start + end)//2
                left = mergeSort(lists, start, mid)
                right = mergeSort(lists, mid+1, end)
                return merge(left, right)
                
        return mergeSort(lists, 0, len(lists)-1)
                
