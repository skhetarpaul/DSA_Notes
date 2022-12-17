# https://leetcode.com/problems/course-schedule/description/
#Read the question, it  simply asks in a dependency graph is it possible to linearly order the verticies?
"""
If yes, return True
Else False
Here, we can use Topo Sort to check if this graph is somehow forming a cycle with Kahn Algo(BFS Topo sort)
"""
from queue import Queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        topo = []
        indeg = [0 for i in range(numCourses)]
        adj = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            a,b = prerequisites[i]
            indeg[a]+=1
            adj[b].append(a)
        
        q = Queue()
        for i in range(numCourses):
            if indeg[i]==0:
                q.put(i)

        while not q.empty():
            temp = q.get()
            topo.append(temp)
            for nbr in adj[temp]:
                indeg[nbr]-=1
                if indeg[nbr]==0:
                    q.put(nbr)
        if len(topo)==numCourses:
            return True
        return False