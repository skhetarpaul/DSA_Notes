# https://leetcode.com/problems/concatenated-words/description/
'''Ideally  this question has to be done with Trie + DP, but simpole DFS and graphs can help us as well.

Try Trie + DP approch
'''


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        worddict = set(words)
        ans = []
        def isConcat(word):
            for i in range(1, len(word)):
                if word[:i] in worddict and (word[i:] in worddict or isConcat(word[i:])):
                    return True
            return False

        for word in words:
            if isConcat(word):
                ans.append(word)
        return ans

