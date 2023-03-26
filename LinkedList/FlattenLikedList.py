from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

# List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.child = None

    def __del__(self):
        if(self.next):
            del self.next

def mergeLL(left, right):
    if left is None:
        return right
    elif right is None:
        return left
    else:
        if left.data<=right.data:
            left.child = mergeLL(left.child, right)
            return left
        else:
            right.child = mergeLL(left, right.child)
            return right
        
def flattenLinkedList(head):
    if head is None or head.next is None:
        return head

        
    down = head
    right = flattenLinkedList(head.next)
    down.next = None
    return mergeLL(down, right)