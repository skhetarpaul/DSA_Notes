from queue import Queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = Queue()
        if endWord not in wordList:
            # print("here")
            return 0
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        q.put((beginWord, 1))
        while not q.empty():
            
            word, d = q.get()
            if word==endWord:
                return d
            else:
                for pos in range(len(word)):
                    for equi in range(97, 123):
                        temp = chr(equi)
                        newword = word[:pos] + temp + word[pos+1:]
                        # print(newword)
                        if newword in wordList:
                            wordList.remove(newword)
                            q.put((newword, d+1))
        return 0


