
# https://leetcode.com/problems/longest-turbulent-subarray/description/
from queue import Queue
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)==1 or min(arr)==max(arr):
            return 1
        i,j = 0,1
        maxsize = 2
        def defineRel(i,j):
            leftGreater = 1 if arr[i]>arr[j] else 0 if arr[i]<arr[j] else -1
            return leftGreater
        leftGreater = defineRel(0,1)
        while j<len(arr)-1:
            print(i,j)
            if leftGreater==1:
                if arr[j+1]>arr[j]:
                    j+=1
                    leftGreater = 0
                    maxsize = max(maxsize, j-i+1)
                else:
                    #less tha or equal to case, compare maxsizes and reinit i,j
                    i = j
                    j+=1
                    while j<len(arr)-1 and arr[i]==arr[j]:
                        i+=1
                        j+=1
                    if j<len(arr)-1:
                        leftGreater = defineRel(i,j)
            elif leftGreater==0:
                if arr[j+1]<arr[j]:
                    j+=1
                    leftGreater = 1
                    maxsize = max(maxsize, j-i+1)
                else:
                    i = j
                    j+=1
                    while j<len(arr)-1 and arr[i]==arr[j]:
                        i+=1
                        j+=1
                    if j<len(arr)-1:
                        leftGreater = defineRel(i,j)
            else:
                #both elements are equal
                i = j
                j+=1
                while j<len(arr)-1 and arr[i]==arr[j]:
                    i+=1
                    j+=1
                if j<len(arr)-1:
                    leftGreater = defineRel(i,j)
        return maxsize


                
