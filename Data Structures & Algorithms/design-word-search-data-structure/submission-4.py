
class WordDictionary:

    # Can use plain dicts to create a trie-like structure
    # A word is complete if "#" is in its keys
    # Dicts keys will be chars and vals will be children of that char
    def __init__(self):
        self.root = {}

    # Iterate down the trie, end word by adding '#' as a key
    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = None
        

    # Use recursive helper
    # Track idx in word & cur node/dict
    def search(self, word: str) -> bool:

        # At each level, word[i] in node means the path up to that char is present
        # If word[i] == '.', we consider all keys in node and return True if any are true; if loop finishes without True, return False
        # If word[i] in node, recurse with i+1 and next dict down
        # If i == len(word), return whether node has '#' in its keys (end of word)
        # Return False
        def dfs(i: int, node: dict) -> bool:
            if i == len(word):
                return node and '#' in node
            
            if word[i] == '.':
                for k, v in node.items():
                    if k != '#' and dfs(i + 1, v):
                        return True
                return False
            
            if word[i] in node:
                return dfs(i+1, node[word[i]])
            
            return False
        
        return dfs(0, self.root)
            
