class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # char count tuples to sublist mapping

        for string in strs:
            curCount = [0] * 26
            for char in string:
                curCount[ord(char) - ord('a')] += 1

            groups[tuple(curCount)].append(string)
        
        return list(groups.values())

# Time O(N * K) where N = # strings & K = len of longest string
# Space O(N)