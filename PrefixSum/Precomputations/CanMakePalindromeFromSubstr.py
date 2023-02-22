'''First, the key is understanding we are allowed to rearrange. Knowing this, we can forget about order and only count the occurences of each letter.
Furthermore, we only care if the count is odd. If it's even, we can place an equal amount of letter on either side:
'aaaac' => 'aacaa'
Since 'a''s count is even (4), we can ignore it.

In order to convert a string to a palindrome using replace, we need only to replace half of the letters. For example,
'abcd' => 'abba' (4 // 2 = 2)
'abcde' => 'abcba' (5 // 2 = 2)
Hence, we only need k to be at least half rounded down.'''
# https://leetcode.com/problems/can-make-palindrome-from-substring/


class Solution:
    def canMakePaliQueries(self, s: str, queries) -> List[bool]:
        #precompute the letter occurences
        n = len(s)
        docc = [[0 for i in range(26)] for j in range(n)]
        for i in range(n):
            docc[i][ord(s[i])-97] = 1

        #calculate prefix sum
        for i in range(1,n):
            for j in range(26):
                docc[i][j] = docc[i][j] + docc[i-1][j]
            # print(docc[i])
        
        def minToPalindrome(arr):
            countOdds = 0
            for i in range(26):
                if arr[i]&1:
                    countOdds+=1
            return math.floor((countOdds)/2)

        def calculateEffectiveIndexes(left, right):
            arr = []
            for i in range(26):
                arr.append(docc[right][i]-docc[left-1][i]) if left>0 else arr.append(docc[right][i])
            return arr
        ans = []
        for li, ri, ki in queries:
            arr = calculateEffectiveIndexes(li, ri)
            
            minr = minToPalindrome(arr)
            # print(arr, minr)
            if ki<minr:
                ans.append(False)
            else:
                ans.append(True)
        return ans


