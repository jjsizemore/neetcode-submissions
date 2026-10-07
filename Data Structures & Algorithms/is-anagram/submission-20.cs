public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;

        var counts = new int[26];

        for (int i = 0; i < s.Length * 2; i++) {
            if (i < s.Length) {
                counts[s[i] - 'a']++;
            } else {
                var idx = t[i - s.Length] - 'a';
                counts[idx]--;
                if (counts[idx] < 0) return false;
            }
        }

        return true;
    }
}
