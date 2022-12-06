'''
A trivial approach to find eventual safe nodes, is to find all ndoes in the graph that have a cycle.
All nodes which donot have a cycle are safe nodes. FYI: https://leetcode.com/problems/find-eventual-safe-states/description/
'''
#this problem is also solved by Topological sort.
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #no of nodes in graph
        n = len(graph)
        visited = [0 for i in range(n)]
        dfsvisited = [0 for i in range(n)]
        safeNodes = []
        check = [0 for i in range(n)]

        def checkDFS(node):
            check[node] = 0
            visited[node] = 1
            dfsvisited[node] = 1
            for nbr in graph[node]:
                if visited[nbr]==0:
                    #Neighbour is never visited
                    if checkDFS(nbr):
                        #Node cannot be a safe if its nbr has a cycle.
                        check[node] = 0
                        return True
                        
                elif visited[nbr]==1 and dfsvisited[nbr]==1:
                    #node contains a cycle
                    check[node] = 0
                    return True

            check[node] = 1
            dfsvisited[node] = 0
        for i in range(n):
            if not visited[i]:
                checkDFS(i)
        for i in range(n):
            if check[i]:
                safeNodes.append(i)
        return safeNodes
