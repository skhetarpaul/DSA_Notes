#Uses 2 recursiove fnctions:
'''
One to pop all elements, following which there is a function whih inserts all the popped elements in their very sorted order
'''
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    
    def sortedInsert(self,s,ele):
        if len(s)==0 or s[-1]<=ele:
            s.append(ele)
            return
        else:
            t = s.pop()
            self.sortedInsert(s, ele)
            s.append(t)
            return
        
    def sorted(self, s):
        # Code here
        if len(s)==0:
            return
        else:
            top = s.pop()
            self.sorted(s)
            self.sortedInsert(s, top)
            



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends