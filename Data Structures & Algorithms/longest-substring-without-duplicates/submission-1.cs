public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int maxLen = 0;
        int l = 0;
        HashSet<char> seen = new HashSet<char>();

        for (int r = 0; r < s.Length; r++) {
            while (seen.Contains(s[r])) {
                seen.Remove(s[l]);
                l++;
            }
            seen.Add(s[r]);
            maxLen = Math.Max(maxLen, r - l + 1);
        }
        return maxLen;
    }
}
