# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/
'''Intuition behind the problem:
The question simply gies a set of queries such that for every equery return yest if there is a path 
with every edge w<limit else return no/False.
Brute force says:
Try BFS/DFS from every start node to end node such that, if we find one such path we can return True
Else we shall return False
Time complexity would be O(Q*N) where q: len of queries and n is the number of nodes in graph.

Can we do better?
Can we somehow sort queries array on the basis of limit weights and then check, considering all edges
 which have their edgeweight < limit HOLDS both vertices in the same CONNECTED COMPONENT.
 Further, connected components GIVE aAN IDEA TO USE UNION FIND ALGORITHM.'''


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def findParent(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]

   

    def union(self, x, y):
        px = self.findParent(x)
        py = self.findParent(y)
        if px==py:
            return 
        else:
            rx = self.rank[px]
            ry = self.rank[py]
            if rx<ry:
                self.parent[px] = py
            elif rx>ry:
                self.parent[py] = px
            else:
                self.parent[px] = py
                self.rank[py]+=1
    

class Solution:
    def distanceLimitedPathsExist(self, n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        edge_list = sorted(edge_list, key = lambda x: x[2])
        queries = [[i[0], i[1]] for i in sorted(enumerate(queries), key = lambda x: x[1][2])]
        print(edge_list)
        print(queries)
        ans = [0]*len(queries)
        ei = 0
        qi = 0
        while  qi<len(queries):
            while ei<len(edge_list) and qi<len(queries) and edge_list[ei][2]<queries[qi][1][2]:
                u, v, dist = edge_list[ei]
                uf.union(u, v)
                ei+=1
            qx, qy = queries[qi][1][0], queries[qi][1][1]
            px = uf.findParent(qx)
            py= uf.findParent(qy)
            if px==py:
                ans[queries[qi][0]] = True
            else:
                ans[queries[qi][0]] = False
            qi+=1
        return ans

