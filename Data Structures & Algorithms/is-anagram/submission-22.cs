public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;

        var counts = new int[26];
        
        foreach (char cur in s) counts[cur - 'a']++;
        foreach (char cur in t) {
            if (--counts[cur - 'a'] < 0) return false;
        }

        return true;
    }
}
