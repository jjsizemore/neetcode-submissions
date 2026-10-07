public class Solution {
    public bool IsValid(string s) {
        if (s.Length % 2 == 1) return false;

        Dictionary<char, char> closer = new(){
            { '{', '}' },
            { '[', ']' },
            { '(', ')' }
        };

        Stack<char> closers = new();

        foreach (var c in s) {
            if (closer.ContainsKey(c)) {
                closers.Push(closer[c]);
            } else {
                if (closers.Count == 0 || closers.Pop() != c) {
                    return false;
                }
            }
        }
        return closers.Count == 0;
    }
}
