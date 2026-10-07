public class Solution {
    public bool IsValid(string s) {
        var stack = new Stack<char>();

        var openers = new Dictionary<char, char>(){
            { '}', '{' },
            { ']', '[' },
            { ')', '(' }
        };

        foreach (char c in s) {
            if (openers.Keys.Contains(c)) {
                if (stack.Count > 0 && stack.Peek() == openers[c])
                    stack.Pop();
                else
                    return false;
            } else {
                stack.Push(c);
            }
        }
        return stack.Count == 0;
    }
}
