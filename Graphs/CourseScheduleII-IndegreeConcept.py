# https://leetcode.com/problems/course-schedule-ii/submissions/853286983/
'''
This can use Detect Cycle in Directed graph, but can also be done using this method.
I calculated indeegree of each node and if node is independent(having no prerequisites), then added it to the Queue.
Traversed through the Queue, as I travelled the node neighbours I decreased their indegrees by 1 each time
If indeg of any nbr becomes 0, append it to the q.
'''

from queue import Queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = Queue()
        indeg = [0]*numCourses
        adj = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            indeg[course]+=1
            adj[pre].append(course)
        visited = [0]*numCourses
        for index, i in enumerate(indeg):
            if i==0:
                visited[index] = 1
                q.put(index)
        # print(adj, indeg)
        ans = []
        if q.empty():
            return ans
        while not q.empty():
            node = q.get()
            ans.append(node)
            for nbr in adj[node]:
                if not visited[nbr]:
                    indeg[nbr]-=1
                    if indeg[nbr]==0:
                        q.put(nbr)
                        visited[nbr] = 1
        return ans if len(ans)==numCourses else []

