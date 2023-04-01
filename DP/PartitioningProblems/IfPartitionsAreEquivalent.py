# https://leetcode.com/problems/scramble-string/description/

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        m = {}
        def recursion(s1, s2):
            if (s1, s2) in m:
                return m[(s1, s2)]
            if not sorted(s1)==sorted(s2):
                return False
            if len(s1)==1:
                return True
            else:
                for i in range(1, len(s1)):
                    if (recursion(s1[:i], s2[:i]) and recursion(s1[i:], s2[i:])) or (recursion(s1[:i], s2[-i:]) and recursion(s1[i:], s2[:-i])):
                        m[(s1, s2)] = True
                        return True
                m[(s1, s2)] = False
                return False
        return recursion(s1, s2)
            