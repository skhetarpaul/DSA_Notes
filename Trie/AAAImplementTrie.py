class Node:
    def __init__(self):
        self.eow = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            else:
                curr = curr.children[w]
        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for p in prefix:
            if p not in curr.children:
                return False
            else:

                curr = curr.children[p]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)