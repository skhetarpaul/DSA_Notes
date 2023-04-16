from queue import Queue
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/

'''Following tutorial hel;ps to understand the intuition behind using Topo sort in every problem:
cover all parents firt and then go to the children.
https://www.youtube.com/watch?v=pSBFqxRVQC0'''
class Solution:
    def largestPathValue(self, colors, edges):
        n = len(colors)
        k = 26
        indeg = [0]*n
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            indeg[v]+=1
        q = Queue()
        for i in range(n):
            if indeg[i]==0:
                q.put(i)
        
        counts = [[0]*26 for i in range(n)]
        for i, c in enumerate(colors):
            counts[i][ord(c)-ord('a')]+=1

        max_count, visited = 0, 0
        while not q.empty():
            u = q.get()
            visited += 1
            for v in adj[u]:
                for i in range(k):
                    counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.put(v)
            max_count = max(max_count, max(counts[u]))
        return max_count if visited==n else -1