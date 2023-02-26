#Given is the base implementation of LRU cache with a Doubly linked List
'''This can as'''

class DLLNode:
    def __init__(self,key,val,prev,next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.next, self.prev = None, None
        return

    def insertAtStart(self, node):
        temp = self.next
        self.next = node
        node.prev = self
        node.next = temp
        temp.prev = node
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.head = DLLNode(-1,-1, None, None)
        self.tail = DLLNode(-1,-1,None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.locdict = {}

    def get(self, key: int) -> int:
        # print(self.locdict, "dictionary to find", key)
        if key in self.locdict:
            node = self.locdict[key]
            nodeval = node.val
            newnode = self.head.insertAtStart(DLLNode(key, nodeval, None, None))
            node.remove()
            self.locdict[key] = newnode
            return nodeval
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.locdict:
            if self.cap>0: #there is an empty space
                newnode = self.head.insertAtStart(DLLNode(key, value, None, None))
                self.cap-=1
                self.locdict[key] = newnode
            else:
                #There implies that thewre is atleasst 1 node
                key_to_remove = self.tail.prev.key 
                self.tail.prev.remove()
                self.locdict.pop(key_to_remove)
                newnode = self.head.insertAtStart(DLLNode(key, value, None, None))
                self.locdict[key] = newnode
        else:
            node = self.locdict[key]
            newnode = self.head.insertAtStart(DLLNode(key, value, None, None))
            node.remove()
            self.locdict[key] = newnode
        # print(self.locdict, key, self.locdict[key], "key inserted")
        return
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)