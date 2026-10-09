class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(string)}#{string}' for string in strs)

    def decode(self, s: str) -> List[str]:
        decodedStrings = []

        start = 0
        stop = 0

        while start < len(s):
            stop = s.find('#', start)
            nextLen = int(s[start:stop])
            start = stop + 1
            stop = start + nextLen
            decodedStrings.append(s[start:stop])
            start = stop        
        
        return decodedStrings

# Time O(N)
# Space O(N)
