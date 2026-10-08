class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # sorted chars to sublist mapping

        for string in strs:
            curHash = ''.join(sorted(string))

            groups[curHash].append(string)
        
        return list(groups.values())

# Time O(nlogn)
# Space O(n)