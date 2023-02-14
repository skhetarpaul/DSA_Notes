# https://leetcode.com/problems/fruit-into-baskets/description/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i,j = 0,0
        n = len(fruits)
        d = {}
        ans = 0
        curr = 0
        # print(fruits)
        while j<n:
            # print(fruits[j])
            #first append into dictionary
            if fruits[j] in d:
                d[fruits[j]]+=1
            else:
                d[fruits[j]] = 1
            curr+=1
            # print(j, d, fruits[j])
            if len(d)<=2:
                ans = max(ans, curr)
            else:
                #less is greater than 
                count = len(d)
                while count>2:
                    #remove ith element, dec count
                    d[fruits[i]]-=1
                    if d[fruits[i]]==0:
                        d.pop(fruits[i])
                        count-=1
                    curr-=1
                    i+=1
                ans = max(ans, curr)
            j+=1
        return ans
