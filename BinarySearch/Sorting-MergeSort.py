#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        i,j = l,m+1
        k = 0
        temp = [None for i in range(r-l+1)]
        
        while i<=m and j<=r:
            if arr[i]<=arr[j]:
                temp[k] = arr[i]
                i+=1
                k+=1
            else:
                temp[k] = arr[j]
                j+=1
                k+=1
        while i<=m:
            temp[k] = arr[i]
            i+=1
            k+=1
        while j<=r:
            temp[k] = arr[j]
            j+=1
            k+=1
        for i in range(l,r+1):
            arr[i] = temp[i-l]
        
        
    def mergeSort(self,arr, l, r):
        #code here
        if l>=r:
            return
        else:
            mid = l + (r-l)//2
            self.mergeSort(arr, l,mid)
            self.mergeSort(arr, mid+1, r)
            self.merge(arr, l, mid, r)
            return
