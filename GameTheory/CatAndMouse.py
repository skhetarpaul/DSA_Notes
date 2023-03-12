# https://leetcode.com/problems/cat-and-mouse/description/
'''A basic problem, if mouse lands at 0-> mouse wins
If mouse==cat: cat wins
Else, if they reach same location again: return 1 then draw
'''

# Naive approah: Top down approach

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        #Naive approach: Recursion and Yop down DP
        dcache = {}
        @cache
        def dp(m, c, moves):
            if moves>4*n + 200:
                return 0
            elif c==m:
                return 2
            elif m==0:
                return 1
            # elif (m,c, moves) in dcache:
            #     return dcache[(m,c,moves)]
            else:
                #mouse moves
                if moves%2==0:
                    canDraw = False
                    for nei in graph[m]:
                        ans = dp(nei, c, moves+1)
                        if ans==1:
                            dcache[(m,c,moves)] = 1
                            return 1

                        elif ans==0:
                            canDraw = True

                    ans = 0 if canDraw else 2
                    dcache[(m,c,moves)] = ans
                    return ans
                else:
                    canDraw = False
                    for nei in graph[c]:
                        if nei!=0:
                            ans = dp(m, nei, moves+1)
                            if ans==2:
                                dcache[(m,c,moves)] = 2
                                return 2
                            elif ans==0:
                                canDraw = True
                    ans = 0 if canDraw else 1
                    dcache[(m,c,moves)] = ans
                    return ans
        return dp(1,2,0)