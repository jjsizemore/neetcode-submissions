class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.start = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.start
        for c in word:
            idx = ord(c) - ord('a')
            node = cur.children[idx]
            if not node:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.start
        for c in word:
            idx = ord(c) - ord('a')
            node = cur.children[idx]
            if not node:
                return False
            cur = cur.children[idx]
        return cur.isWord


    def startsWith(self, prefix: str) -> bool:
        cur = self.start
        for c in prefix:
            idx = ord(c) - ord('a')
            node = cur.children[idx]
            if not node:
                return False
            cur = cur.children[idx]
        return True

    # Time O(n), n = len(string)
    # Space O(t), t = # TrieNodes
        