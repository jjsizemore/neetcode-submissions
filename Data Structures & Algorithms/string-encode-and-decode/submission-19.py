class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        decodedStrings = []

        while i < len(s):
            delim = s.find('#', i)
            length = int(s[i : delim])
            decodedStrings.append(s[delim + 1 : delim + 1 + length])
            i = delim + 1 + length
        
        return decodedStrings

# Time O(N)
# Space O(N)