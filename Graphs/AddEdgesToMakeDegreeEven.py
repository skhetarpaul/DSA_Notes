#Only complication is to list all edgecases here and find all vertices with odd degrees and list the cases as below.
# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/submissions/861547914/

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = [set() for i in range(n)]
        for a,b in edges:
            adj[a-1].add(b-1)
            adj[b-1].add(a-1)
        count = 0 #to count the number of vertex with odd degree
        odds = []
        for i in range(n):
            if len(adj[i])%2==1: #odd
                count+=1
                odds.append(i)

        if count%2==1 or count>4: #odd
            # print(count)
            return False
        elif count==0:
            return True
        else:
            if count==2:
            
                a = odds[0]
                b = odds[1]
                if a not in adj[b]:
                    return True
                for i in range(n):
                    if i in adj[a] or i in adj[b]:
                        continue
                    return True
                return False
            else:
                a,b,c,d = odds[0],odds[1],odds[2],odds[3]
                if a not in adj[b] and c not in adj[d]:
                    return True
                elif a not in adj[c] and d not in adj[b]:
                    return True
                elif a not in adj[d] and b not in adj[c]:
                    return True
                return False
                
                        
            
            