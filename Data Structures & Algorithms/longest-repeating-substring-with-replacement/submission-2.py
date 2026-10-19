class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # simpler version would be looking for longest substring of all 1 character
        # sliding window where we maintain counts of chars?
        # valid substring only has 1 key with a value > 1
        # for replacement, we also consider substrings with up to k other chars valid
        # check # other chars by subtracting main char count from length

        count = defaultdict(int)
        max_freq = 0
        res = 0
        i = 0

        for j, c in enumerate(s):
            count[c] += 1

            max_freq = max(max_freq, count[c])

            other_chars_count = j - i + 1 - max_freq
                        
            if k >= other_chars_count:
                res = max(res, j - i + 1)
            else:
                count[s[i]] -= 1
                max_freq = max(count.values())
                i += 1

        return res