# https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
from collections import deque

def printFirstNegativeInteger( A, N, K):
    # code here
    arr = A
    ans = []
    q = deque()
    i,j = 0,0
    while j<N:
        if arr[j]<0:
            q.append([arr[j],j])
        if j-i+1<K:
            j+=1
        else:
            if len(q)==0:
                ans.append(0)
            else:
                neg = q.popleft()
                ans.append(neg[0])
                if i<neg[1]:
                    q.appendleft(neg)
            i+=1
            j+=1
    return ans
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends