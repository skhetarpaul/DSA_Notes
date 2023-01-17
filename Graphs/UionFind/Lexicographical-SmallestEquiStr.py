# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/submissions/

'''Looking at the question, it could be esasily inferred that somehow I need to work with dictionary and make groups of similar characters of which THERE COULD BE ONLY ONE parent.PendingDeprecationWarningHence clicks, the idea of Union Find algorthm'''

class UnionFind:
    def __init__(self, uniques):
        self.parent = {i:i for i in uniques}
        # print(self.parent)

    def findParent(self, x):
        if x not in self.parent:
            # print(x)
            return x
        elif self.parent[x]!=x:
            self.parent[x] = self.findParent(self.parent[x])
        # print("parent of {} is  {}".format(x, self.parent[x]))
        return self.parent[x]
    
    def union(self, x, y):
        px = self.findParent(x)
        py = self.findParent(y)
        if px==py:
            return
        else:
            if ord(px)<ord(py):
                self.parent[py] = px
            else:
                self.parent[px] = py
        # print(self.parent)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uniques = set()
        for i in range(len(s1)):
            uniques.add(s1[i])
            uniques.add(s2[i])

        UF = UnionFind(uniques)
        for i in range(len(s1)):
            c1,c2 = s1[i], s2[i]
            # print("case: {}- {}".format(c1, c2))
            UF.union(c1, c2)

        # print(UF.parent)
        ans = ''
        for ch in baseStr:
            ans+=UF.findParent(ch)
        return ans
