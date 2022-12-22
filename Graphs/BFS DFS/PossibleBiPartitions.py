from queue import Queue

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        
        colors = [-1 for i in range(n)]
        adj = [set() for i in range(n)]
        for x,y in dislikes:
            adj[x-1].add(y-1)
            adj[y-1].add(x-1)
        def BFS(node):
            q = Queue()
            q.put(node)
            colors[node] = 0
            while not q.empty():
                temp = q.get()
                for nbr in adj[temp]:
                    if colors[nbr]==colors[temp]:
                        return False
                    elif colors[nbr]==-1:
                        colors[nbr] = 1-colors[temp]
                        q.put(nbr)
            return True


        for i in range(n):
            if colors[i]==-1:
                if not BFS(i):
                    return False
        return True