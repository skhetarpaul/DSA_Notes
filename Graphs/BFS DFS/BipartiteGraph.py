#BFS:

from queue import Queue

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = Queue()
        n = len(graph)
        #-1 represents no color. 0 and 1 will be 2 colors
        visited = [-1 for i in range(n)]
        for i in range(n):
            if visited[i]==-1:
                #Assign the node a color
                visited[i] = 0
                q.put(i)
                while not q.empty():
                    node = q.get()
                    for nbr in graph[node]:
                        if visited[nbr]!=-1 and visited[nbr]==visited[node]:
                            return False
                        elif visited[nbr]==-1:
                            visited[nbr] = not visited[node]
                            q.put(nbr)
        return True





#DFS
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        #-1 represents no color. 0 and 1 will be 2 colors
        visited = [-1 for i in range(n)]
        def DFS(node):
            for nbr in graph[node]:
                if visited[nbr]!=-1 and visited[nbr]==visited[node]:
                    return False
                elif visited[nbr]==-1:
                    visited[nbr] = not visited[node]
                    if not DFS(nbr):
                        return False
            return True 

        for i in range(n):
            if visited[i]==-1:
                #Assign the node a color
                visited[i] = 0
                if not DFS(i):
                    return False
        return True