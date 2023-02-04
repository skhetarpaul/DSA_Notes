# Folllow up question to Alien Dictionary - Leetcode HARD
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dorder = {o: index for index, o in enumerate(order)}
        print(dorder)
        dorder['phi'] = -1
        def findOrder(s1, s2):
            minl = min(len(s1), len(s2))
            for i in range(minl):
                if s1[i]==s2[i]:
                    continue
                else:
                    #Suggesting dict order of words s1[i]> s2[i]
                    return (s1[i], s2[i])
            if minl==len(s1)==len(s2):
                return ('phi', 'phi')
            elif minl==len(s1):
                return ('phi',s2[minl])
            else:
                return (s1[minl], 'phi')
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            diffw1, diffw2 = findOrder(w1, w2)
            print(diffw1, diffw2, dorder[diffw1],dorder[diffw2])
            if dorder[diffw1]>dorder[diffw2]:
                return False
        return True

            