# https://leetcode.com/problems/network-delay-time/description/
# Refer this answer for an implementation of Dijkstra algorithm thru Priority Queue.


import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        adj = [set() for i in range(n)]
        for u,v,w in times:
            adj[u-1].add((v-1,w))
        dist = [float("inf") for i in range(n)]
        dist[k-1] = 0
        pq = []
        heapq.heappush(pq, [0,k-1])
        while not len(pq)==0:
            d, node = heapq.heappop(pq)
            for nbr, nbrd in adj[node]:
                if d + nbrd<dist[nbr]:
                    dist[nbr] = d + nbrd
                    heapq.heappush(pq, [dist[nbr],nbr])
        for i in range(n):
            if dist[i]==float("inf"):
                dist[i] = -1
                return -1
        # print(dist)
        return max(dist)
