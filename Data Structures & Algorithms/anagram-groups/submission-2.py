class Solution:
    def findHash(self, string: str):
        return ''.join(sorted(string))


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Finding anagram is a solved problem, count occurrences of each char
        # Is there a way to efficiently associate the char counts of each string in one sublist with that sublist
        # Could just compose a "hash" string after determining counts by enumerating over the counts array & concat. idx+array for each

        groups = []

        hashToIdx = {}

        for string in strs:
            curHash = self.findHash(string)

            if curHash in hashToIdx:
                groups[hashToIdx[curHash]].append(string)
            else:
                groups.append([string])
                hashToIdx[curHash] = len(groups) - 1
        return groups



    