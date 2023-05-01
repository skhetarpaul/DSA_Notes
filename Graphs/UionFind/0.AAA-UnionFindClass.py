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
