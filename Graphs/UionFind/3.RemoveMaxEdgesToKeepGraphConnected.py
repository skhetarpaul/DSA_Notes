'''
A stepwise approach for the problem is given below:
1. We need to remove maximum edges from the graph keeping the graph connected.
2. This is equivalent to create a minimum edge tree keeping the graph connected.
3. Also, since we have 3 type of edges i.e. 1, 2, 3 but we must notice that adding an edge 3 is of maximum benefit
As this edge can be used by both A and B
4. But how to check if two nodes in the graph are already connected or do we need to connect them with the edge. 
Union Find Algorithm helps here.

https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/
https://www.youtube.com/watch?v=ukLyFDlBFW0'''


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def findParent(self, node):
        if self.parent[node]!= node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, t1, t2):
        pa = self.findParent(t1)
        pb = self.findParent(t2)
        if pa==pb:
            return
        else:
            ra = self.rank[pa]
            rb = self.rank[pb]
            if ra>rb:
                self.parent[pb] = pa
            elif rb>ra:
                self.parent[pa] = pb
            else:
                self.parent[pa] = pb
                self.rank[pb]+=1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        nodes_alice = 0
        nodes_bob = 0
        removed = 0
        aliceconnects = UnionFind(n)
        bobconnects = UnionFind(n)
        for t, u, v in edges:
            u = u-1
            v = v-1
            if t==3:
                #check for alice
                if aliceconnects.findParent(u)!=aliceconnects.findParent(v):
                    #node needs to be included
                    aliceconnects.union(u, v)
                    bobconnects.union(u, v)
                    nodes_alice+=1
                    nodes_bob+=1
                else:
                    removed+=1
        

        for t, u, v in edges:
            u = u-1
            v = v-1
            if t==1:
                #check for alice
                if aliceconnects.findParent(u)!=aliceconnects.findParent(v):
                    #node needs to be included
                    aliceconnects.union(u, v)
                    nodes_alice+=1
                else:
                    removed+=1
            elif t==2:
                #check for bob
                if bobconnects.findParent(u)!=bobconnects.findParent(v):
                    #node needs to be included
                    bobconnects.union(u, v)
                    nodes_bob+=1
                else:
                    removed+=1
        return removed if (nodes_alice==n-1 and nodes_bob==n-1) else -1