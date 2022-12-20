from queue import Queue

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Brute force Algorithm utilizing BFS algorithm(TLE)
        q = Queue()
        q.put((0,0))
        adj = [set() for i in range(n)]
        for x,y,d in roads:
            adj[x].add((y,d))
            adj[y].add((x,d))
        count = 0
        # visited = [0 for i in range(n)]
        distance = [float("inf") for i in range(n)]
        distance[0] = 0
        while not q.empty():
            s = q.qsize()
            for i in range(s):
                node, dist = q.get()
                if node==n-1:
                    #check for condition and update smallest distance
                    if dist<distance[n-1]:
                        distance[n-1] = dist
                        count = 1
                    elif dist==distance[n-1]:
                        count+=1
                else:
                    for nbr,d in adj[node]:
                        if dist + d<=distance[nbr]:
                            distance[nbr] = dist + d
                            q.put((nbr,distance[nbr]))
        mod = (10**9+7)
        return count%mod

