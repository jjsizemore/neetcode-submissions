class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        res = 0
        i = 0

        for j, c in enumerate(s):
            count[c] += 1

            while count[c] > 1:
                count[s[i]] -= 1
                i += 1

            res = max(res, j - i + 1)
        
        return res