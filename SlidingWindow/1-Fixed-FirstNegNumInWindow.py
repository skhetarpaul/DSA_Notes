#User function Template for python347

'''Important points to ponder over:
Why deque: Because I want control over left elements as well. I want to see what is q[0]
'''
from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    q = deque()
    i, j=0,0
    ans = []
    while j<N:
        if A[j]<0:
            q.append(j)
        if j-i+1<K:
            j+=1
        else:
            if not len(q)==0 and q[0]<j-K+1:
                q.popleft()
            if len(q)==0:
                ans.append(0)
            else:
                ans.append(A[q[0]])
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