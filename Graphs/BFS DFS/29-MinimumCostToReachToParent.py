# An important question helping to think the way of collecting of node representatives.
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/solutions/3080167/minimum-fuel-cost-to-report-to-the-capital/?orderBy=most_relevant
import math

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.fuel = 0
        adj = [set() for i in range(len(roads)+1)]

        for rx, ry in roads:
            adj[rx].add(ry)
            adj[ry].add(rx)

        def DFS(node, parent):
            representatives = 1
            for child in adj[node]:
                if child!=parent:
                    representatives+=DFS(child, node)
            if node!=0:
                self.fuel+=math.ceil(representatives/seats)
            return representatives
        DFS(0, -1)
        return self.fuel