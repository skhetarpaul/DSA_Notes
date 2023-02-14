'''https://leetcode.com/problems/search-a-2d-matrix/description/

Noteworthy points:
    How rownum, colnum is calculated === (mid//m, mid%m) where m is the number of columns
    
    Also, note the=at if you write 2d matrix in left to right fashion, you will get a sorted matrix.'''

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        n = len(matrix) #row
        m = len(matrix[0]) #column
        low = 0
        high = n*m-1
        while low<=high:
            mid = (low + high)//2
            rowindex = mid//m #mid//colnum
            colindex = mid%m
            if matrix[rowindex][colindex]==target:
                return True
            elif matrix[rowindex][colindex]<target:
                low = mid+1
            else:
                high = mid-1
            
        return False