'''https://leetcode.com/problems/search-a-2d-matrix-ii/description/
This problem is a little different from other one,. You start with an element at (0,m-1)
 where n is rownum, m is colnum. And we see if this is equivalent to the target, if yes simply return Yes else 
 if element>target:
        We will move left, j-=1
if element<target:
        We will move down, i+=1
    
    '''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #Start from i=0, j=m-1 where m is column num
        n = len(matrix)
        m = len(matrix[0])
        
        j = m-1
        i = 0
        while j>=0 and i<n:
            ele = matrix[i][j]
            #In the while looping condition, we maintained edge case until we are out of looping bounds, till that point we can continue to run the loop
            if ele==target:
                return True
            elif ele>target:
                j-=1
            else:
                i+=1

        return False
