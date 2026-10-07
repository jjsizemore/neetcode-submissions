public class Solution {
    private Stack<int> _stack = new();
    private HashSet<string> _set = new(){ "+", "-", "*", "/" };
    public int EvalRPN(string[] tokens) {
        foreach (string c in tokens)
        {
            if (_set.Contains(c)) {
                int second = _stack.Pop();
                int first = _stack.Pop();
                int res;
                if (c == "+") 
                {
                    res = first + second;
                } 
                else if (c == "-")
                {
                    res = first - second;
                }
                else if (c == "*")
                {
                    res = first * second;
                }
                else
                {
                    res = Convert.ToInt32((first / second));
                }
                _stack.Push(res);
                continue;
            } else {
                _stack.Push(Convert.ToInt32(c));
            }
        }
        return _stack.Peek();
    }
}
