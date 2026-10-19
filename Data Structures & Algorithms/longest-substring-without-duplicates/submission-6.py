class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        last_idx = {}

        for j, c in enumerate(s):
            if c in last_idx:
                i = max(i, last_idx[c] + 1)
            last_idx[c] = j

            res = max(res, j - i + 1)
        
        return res