class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for string in strs:
            encodedString += f"{len(string)}#{string}"
        return encodedString

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



            
