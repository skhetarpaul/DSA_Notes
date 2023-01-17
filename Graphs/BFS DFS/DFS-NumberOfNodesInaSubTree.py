# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/submissions/
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = [set() for i in range(n)]

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        ans = [0 for i in range(n)]
        visited = [0 for i in range(n)]
        def DFS(node):
            visited[node] = True
            alp = [0 for i in range(26)]
            alp[ord(labels[node])-97]+=1
            for nbr in adj[node]:
                if not visited[nbr]:
                    alphNbr = DFS(nbr)
                    # for key, val in alp.items():
                    #     alp[key]+=alphNbr[key]
                    for i in range(26):
                        alp[i]+=alphNbr[i]
            ans[node] = alp[ord(labels[node])-97]
            # print("node is {} and alp is {}".format(node, alp))
            return alp
        DFS(0)
        return ans
