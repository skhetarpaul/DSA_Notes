# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        @cache
        def recursion(index, curr, arr):
            # print("index = {} curr = {} and arr = {}".format(index, curr, arr))
            if index==n:
                if curr=="":
                    ans.append(arr)
            
            else:
                #consider the part into current partition and continue
                
                recursion(index+1, curr + s[index], arr)
                #if a palindrome, take partition into array and move with empty current
                stemp = curr + s[index]
                if stemp==stemp[::-1]:
                    recursion(index+1, "", arr + [stemp])
                return
        recursion(0, "",[])
        return ans