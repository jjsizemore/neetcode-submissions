class TrieNode:
    def __init__(self, isWord: bool = False):
        self.children = {}
        self.isWord = isWord

class WordDictionary:
    # Starts off with a root node
    # Each node will have a dict where key is a valid char in the path
    # Each node repr. a char
    # Node that contains last char of word has flag isWord = True
    def __init__(self):
        self.root = TrieNode()

    # Iterate down a path, adding/modifying nodes to/in the children dict at each level
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode()
                cur = cur.children[c]

        cur.isWord = True
        
    # First char of word must be in node.children, starting with node = root
    # For queries with '.', have to consider all chars at that level
    # Can be implemented as DFS helper with a for loop on '.'
    # Recurse on successful match with word[1:]
    # If not word & node.isWord return True
    def search(self, word: str) -> bool:
        
        def dfs(i: int, node: TrieNode):
            if i == len(word):
                return node.isWord
            
            # word[i] is wildcard, try all children
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True

            if word[i] in node.children:
                return dfs(i + 1, node.children[word[i]])
            
            return False

        return dfs(0, self.root)


