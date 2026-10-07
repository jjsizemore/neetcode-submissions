public class Solution {
    public bool IsValid(string s) {
        Stack<char> rights = new();
        Dictionary<char, char> toRight = new(){
            { '{', '}' },
            { '[', ']' },
            { '(', ')' }            
        };


        foreach (char c in s) {
            if (toRight.ContainsKey(c)) {
                rights.Push(toRight[c]);
            } else if (rights.Count == 0 || rights.Pop() != c) {
                return false;
            }
        }

        return rights.Count == 0;
    }
}
