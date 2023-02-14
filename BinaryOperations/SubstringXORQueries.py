
# https://leetcode.com/problems/substring-xor-queries/description/
'''One Brute force way to do this question is to go to each of the query, find the resultant xor string and find the same with Sliding window in the string s.
This takes O(len(queries)*O(len(s))). This approach gives a TLE

Finally, If I think to do the O(len(s)) in a constant time, I should be able to reach a desired complexity.
For that, calculate eah substring in dictionary and store its left, right endpoints separately.

One point worth to note is, this should be a O(32*len(s)) operation as no Binary number can cross 32 bits as given in the constraints. 
This can be further clarified, when you take a look at line: 17'''
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        dnums = {}
        n  = len(s)
        for i in range(n):
            for j in range(i, min(32 + i, n)):
                sub = s[i:j+1]
                sub = "0b" + sub
                if sub in dnums:
                    continue
                else:
                    dnums[sub] = [i,j]
        
        # print(dnums, len(dnums))
        ans = []
        for qi, qj in queries:
            qres = qi^qj
            binres = bin(qres)
            # print(binres)
            if binres in dnums:
                ans.append(dnums[binres])
            else:
                ans.append([-1,-1])
                
        return ans