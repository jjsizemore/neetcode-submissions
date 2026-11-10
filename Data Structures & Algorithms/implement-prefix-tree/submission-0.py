class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.children = {}
        self.isWord = False


class PrefixTree:

    def __init__(self):
        self.start = TrieNode('dummy')


    def insert(self, word: str) -> None:
        cur = self.start
        for c in word:
            if c not in cur.children:
                cur.children[c] = (TrieNode(c))
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.start
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.start
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return True

        