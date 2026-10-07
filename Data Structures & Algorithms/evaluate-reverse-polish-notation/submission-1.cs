public class Solution {
    public int EvalRPN(string[] tokens) {
        Stack<int> stack = new();

        foreach(string op in tokens) {
            if (op == "+") {
                stack.Push(stack.Pop() + stack.Pop());
            } else if (op == "-") {
                int a = stack.Pop();
                int b = stack.Pop();
                stack.Push(b - a);
            } else if (op == "*") {
                stack.Push(stack.Pop() * stack.Pop());
            } else if (op == "/") {
                int a = stack.Pop();
                int b = stack.Pop();
                stack.Push((int) b / a);
            } else {
                stack.Push(int.Parse(op));
            }
        }
        return stack.Pop();
    }
}
