public class Solution {
    public bool IsAnagram(string s, string t) {
        int[] count = new int[26];

        foreach (char c in s) count[c - 'a']++;

        foreach (char d in t) {
            if (count[d - 'a']-- == 0) return false;
        }
        
        return count.Sum() == 0;
    }
}
