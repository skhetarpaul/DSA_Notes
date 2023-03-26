# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1

#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        ele = A[0]
        occ = 1
        for i in range(1, N):
            if A[i]==ele:
                occ+=1
            else:
                occ-=1
            if occ==0:
                ele = A[i]
                occ = 1
        occ = 0
        for i in range(N):
            if A[i]==ele:
                occ+=1
        return ele if occ>N//2 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends