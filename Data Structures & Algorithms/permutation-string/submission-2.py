class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count all chars in s1
        # move a fixed length sliding window through s2 and if a char is a key in the counter dict, decrement its count
        # if all counts are <= 0, return true
        # since all chars are lowercase, can use 26 len array as counter too

        count = [0] * 26

        for c in s1:
            idx = ord(c) - ord('a')
            count[idx] += 1

        for j in range(len(s2)):
            idx = ord(s2[j]) - ord('a')
            count[idx] -= 1
            
            if j >= len(s1):
                char_to_remove = s2[j - len(s1)]
                idx = ord(char_to_remove) - ord('a')
                count[idx] += 1

            if all(x <= 0 for x in count):
                return True

        return False