'''The only catch is to use a frequency array to catch, how many possible number of combinations can be made at a particular index.(SSee problem description for better uderstanding)'''

'''Note: Good job: Took hints online, but DIY.
https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/
'''

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9+7
        freq = [[0 for i in range(len(words[0]))] for j in range(26)]

        for i in range(len(words)):
            for j in range(len(words[0])):
                # print(words[i][j])
                freq[ord(words[i][j]) - ord('a')][j]+=1
        n = len(words[0])
        m = len(target)
        @cache
        def func(index, lastocc):
            if index==m:
                return 1
            elif lastocc==len(words[0]):
                return 0
            else:
                ans = 0
                numocc = freq[ord(target[index]) - ord('a')][lastocc]
                ans += numocc*func(index+1,lastocc+1)
                ans+= func(index, lastocc+1)
                # for k in range(lastocc, n):
                #     # print(ord(target[index]) - ord('a'))
                #     numocc = freq[ord(target[index]) - ord('a')][k]
                #     ans += numocc*func(index+1,k+1)
                ans = ans%MOD
                return ans
        return func(0, 0)

        def Tabulation():
            dp = [[0 for i in range(n)] for j in range(m)]
            for index in range(m, -1,-1):
                for lastocc in range(n, -1,-1):
                    if index==m:
                        dp[index][lastocc] = 1
                    elif lastocc==n:
                        dp[index][lastocc] = 0
                    else:
                        ans = 0
