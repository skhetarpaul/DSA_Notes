# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        curr.eow = True

    def keySearch(self, word, curr):
        for i,w in enumerate(word):
            if w!='.':
                if w not in curr.children:
                    return False
                else:
                    curr = curr.children[w]
            else:
                
                for c, cnode in curr.children.items():
                    ans = self.keySearch(word[i+1:], cnode)
                    if ans==True:
                        return True
                return False
        return True if curr.eow else False

    def search(self, word: str) -> bool:
        curr = self.root
        for i,w in enumerate(word):
            if w!='.':
                if w not in curr.children:
                    return False
                else:
                    curr = curr.children[w]
            else:
                #w = '.'
                ans = False
                for c, cnode in curr.children.items():
                    ans = ans or self.keySearch(word[i+1:], cnode)
                return ans

        return True if curr.eow else False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)