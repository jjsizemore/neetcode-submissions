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

        matches = 0
        for c in count:
            matches += (1 if not c else 0)

        for j in range(len(s1), len(s2)):
            if matches == 26:
                return True

            count[ord(s2[j - len(s1)]) - ord('a')] += 1
            if count[ord(s2[j - len(s1)]) - ord('a')] == 0:
                matches += 1
            elif count[ord(s2[j - len(s1)]) - ord('a')] == 1:
                matches -= 1

            count[ord(s2[j]) - ord('a')] -= 1
            if count[ord(s2[j]) - ord('a')] == 0:
                matches += 1
            elif count[ord(s2[j]) - ord('a')] == -1:
                matches -= 1

        return matches == 26