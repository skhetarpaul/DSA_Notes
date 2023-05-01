'''Contains two approahes for impleemnting a minstack:
First one is a naive approach using 2 stacks i.e. 0(n) and O(n) space.
Second approach O(n) time and o(1) space'''

# Approach 1:
class MinStack:

    def __init__(self):
        self.stk = []
        self.ss = []

    def push(self, val: int) -> None:
        if len(self.stk)==0 or self.ss[-1]>=val:
            print(val, "values")
            self.stk.append(val)
            self.ss.append(val)
        else:
            self.stk.append(val)

    def pop(self) -> None:
        if len(self.stk)==0:
            return
        elif self.stk[-1]==self.ss[-1]:
            self.stk.pop()
            self.ss.pop()
        else:
            self.stk.pop()

    def top(self) -> int:
        if len(self.stk)==0:
            return -1
        else:
            return self.stk[-1]

    def getMin(self) -> int:
        if len(self.ss)>0:
            return self.ss[-1]
        else:
            return -1



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Approach 2
class MinStack:

    def __init__(self):
        self.stk = []
        self.minele = None

    def push(self, val: int) -> None:
        if len(self.stk)==0:
            self.minele = val
            self.stk.append(val) 
        elif val<=self.minele:
            self.stk.append(2*val-self.minele)
            self.minele = val
        else:
            self.stk.append(val)
            

    def pop(self) -> None:
        if len(self.stk)==0:
            return
        else:
            if self.stk[-1]<=self.minele:
                self.minele = 2*self.minele - self.stk[-1]
            self.stk.pop()

    def top(self) -> int:
        if len(self.stk)==0:
            return -1
        else:
            if self.stk[-1]<self.minele:
                return self.minele
            else:
                return self.stk[-1]

    def getMin(self) -> int:
        if self.minele  !=-1:
            return self.minele
        else:
            return -1



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()