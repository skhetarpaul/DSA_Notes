# https://leetcode.com/problems/similar-string-groups/description/
'''Easy intuition, just use brute force.
Also, best way to find connected components is Union Find algorithm :)'''

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.count = n

    
    def findParent(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, a, b):
        pa = self.findParent(a)
        pb = self.findParent(b)
        if pa==pb:
            return 
        else:
            ra, rb = self.rank[pa], self.rank[pb]
            if ra>rb:
                self.parent[pb] = pa
            elif rb>ra:
                self.parent[pa] = pb
            else:
                self.rank[pb]+=1
                self.parent[pa] = pb
            self.count-=1


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(x, y):
            if x==y:
                return True
            else:
                count = 0
                for i in range(k):
                    if x[i]!=y[i]:
                        count+=1
                        if count>2:
                            return False
                return count==2

        uf = UnionFind(len(strs))
        n = len(strs)
        k = len(strs[0])
        for i in range(n):
            for j in range(i+1, n):
                if isSimilar(strs[i], strs[j]):
                    uf.union(i, j)
        return uf.count
