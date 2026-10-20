class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count all chars in s1
        # move a fixed length sliding window through s2 and if a char is a key in the counter dict, decrement its count
        # if all counts are <= 0, return true
        # since all chars are lowercase, can use 26 len array as counter too

        if len(s1) > len(s2):
            return False

        count = [0] * 26

        for i in range(len(s1)):
            i1 = ord(s1[i]) - ord('a')
            count[i1] += 1
            i2 = ord(s2[i]) - ord('a')
            count[i2] -= 1

        for j in range(len(s1), len(s2)):
            if not any(count):
                return True

            count[ord(s2[j - len(s1)]) - ord('a')] += 1
            count[ord(s2[j]) - ord('a')] -= 1

        return not any(count)