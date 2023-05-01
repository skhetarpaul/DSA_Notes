class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        @cache
        def lcs(index1, index2):
            if index1==n or index2==n:
                return 0
            else:
                if s1[index1]==s2[index2]:
                    return 1 + lcs(index1+1, index2+1)
                else:
                    return max(lcs(index1+1, index2), lcs(index1, index2+1))
        s1 = s
        s2 = s[::-1]
        return n-lcs(0, 0)