

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def findParent(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        parentx = self.findParent(x)
        parenty = self.findParent(y)
        if parentx==parenty:
            return
        else:
            if self.rank[parentx]<self.rank[parenty]:
                self.parent[parentx] = parenty
            elif self.rank[parenty]<self.rank[parentx]:
                self.parent[parenty] = parentx
            else:
                self.parent[parenty] = parentx
                self.rank[parentx]+=1
    
                
        
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        UF = UnionFind(n)
        adj = [[] for i in range(n)]
        for x,y in dislikes:
            adj[x-1].append(y-1)
            adj[y-1].append(x-1)

        for node in range(0,n):
            for nbr in adj[node]:
                if UF.findParent(node)==UF.findParent(nbr):
                    return False
                UF.union(adj[node][0], nbr)
        return True
                