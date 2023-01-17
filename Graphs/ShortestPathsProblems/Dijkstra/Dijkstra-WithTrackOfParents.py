#User function Template for python3

'''The slight change from the originsl algorithm is that, here we are maintaining og the parent array.'''
import heapq
class Solution:
    def shortestPath(self, n, m, edges):
        # Code here
        adj = [set() for i in range(n+1)]
        for u,v,wt in edges:
            adj[u].add((v,wt))
            adj[v].add((u, wt))
        
        dist = [float("inf") for i in range(n+1)]
        dist[1] = 0
        parent = [i for i in range(n+1)]
        
        pq = []
        heapq.heappush(pq, (0,1))
        while len(pq)>0:
            w, node = heapq.heappop(pq)
            for nbr, nwt in adj[node]:
                if nwt + w<dist[nbr]:
                    dist[nbr] = nwt + w
                    parent[nbr] = node
                    heapq.heappush(pq, (dist[nbr], nbr))
        if dist[n]==float("inf"):
            return [-1]
        else:
            # print(parent, dist)
            node = n
            ans = [n]
            while parent[node]!=node:
                ans.append(parent[node])
                node = parent[node]
            return ans[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends