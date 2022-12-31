'''A modified dijkstra algorithm takinmg into consideration two cases for counting distances oif different nodes in ways array:
    if distance + nbr(d)< distance[nbr]:
        update the ways to ways[node]
    elif distance + nbr(d)==distance[nbr]:
        Add ways=> ways[nbr] = wys[nbr] + ways[node]
'''



import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9+7
        ways = [0 for i in range(n)]
        adj = [set() for i in range(n)]
        distance = [float("inf") for i in range(n)]
        for x,y,d in roads:
            adj[x].add((y,d))
            adj[y].add((x,d))
        distance[0] = 0
        q = []
        ways[0] = 1
        heapq.heappush(q, (0,0)) #in form of distance, node

        while len(q)!=0:
            dist, node = heapq.heappop(q)
            for nbr,d in adj[node]:
                if dist + d<distance[nbr]:
                    distance[nbr] = dist + d
                    ways[nbr] = ways[node]%mod
                    heapq.heappush(q, (distance[nbr], nbr))
                elif dist + d==distance[nbr]:
                    ways[nbr]=(ways[node] + ways[nbr])%mod
        return ways[n-1]
                

