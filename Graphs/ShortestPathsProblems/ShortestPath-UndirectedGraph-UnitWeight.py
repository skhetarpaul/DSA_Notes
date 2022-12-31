#User function Template for python3
from queue import Queue
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = [[] for i in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        distance = [float("inf") for i in range(n)]
        distance[src] = 0
        q = Queue()
        
        q.put((src,0))
        while not q.empty():
            node, d = q.get()
            for nbr in adj[node]:
                if distance[nbr]>distance[node] + 1:
                    distance[nbr] = distance[node] + 1
                    q.put((nbr, distance[nbr]))
        for i in range(n):
            if distance[i]==float("inf"):
                distance[i] = -1
        return distance

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends