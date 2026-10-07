public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> groups = new();

        foreach (string str in strs) {
            string hash = createHash(str);
            if (!groups.ContainsKey(hash))
                groups[hash] = new List<string>();
            groups[hash].Add(str);
        }
        return groups.Values.ToList();
    }

    private string createHash(string str) {
        int[] counts = new int[26];

        foreach (char c in str)
            counts[c - 'a']++;
        
        return string.Join('-', counts);
    }
}
