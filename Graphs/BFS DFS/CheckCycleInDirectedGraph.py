#User function Template for python3
from queue import Queue

class Solution:
    def checkDFS(self, visited, dfsVisited, adj, i):
        visited[i] = 1
        dfsVisited[i] = 1
        for nbr in adj[i]:
            if visited[nbr]==0:
                if self.checkDFS(visited, dfsVisited, adj, nbr)==True:
                    return True
            elif visited[nbr]==1 and dfsVisited[nbr]==1:
                return True
        dfsVisited[i] = 0
        return False
                
                
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = [0 for i in range(V)]
        dfsVisited = [0 for i in range(V)]
        for i in range(V):
            if visited[i]==0:
                if self.checkDFS(visited, dfsVisited, adj, i):
                    return True
        return False
                
            
                    
                
        
    
