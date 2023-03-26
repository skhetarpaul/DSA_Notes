# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
'''Understand the question: It says that the minimum distance node needs to be calculated in the connected graph rom node 1. This is straightforward DFS approach.

Other approach, is wrii=tten here: Modified Dijkstra where we calculate the minimum score between every 2 nodes'''
import heapq
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for x,y,d in roads:
            adj[x-1].append((y-1, d))
            adj[y-1].append((x-1, d))
        distance = [float("inf") for i in range(n)]
        # distance[0] = 0
        q = []
        heapq.heappush(q, (float("inf"),0)) #distance[node], node
        while not len(q)==0:
            td, node = heapq.heappop(q)
            for nbr, nbrd in adj[node]:
                if distance[nbr]>min(nbrd, td):
                    distance[nbr] = min(nbrd, td)
                    heapq.heappush(q, (distance[nbr], nbr))
        return distance[n-1]


