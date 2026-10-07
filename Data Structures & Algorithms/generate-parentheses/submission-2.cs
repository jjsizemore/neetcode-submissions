public class Solution {  
    public List<string> GenerateParenthesis(int n) {
        // Can use backtracking
        // Valid strings must have opening parentheses before closing
        // If openers < n, can add opener
        // If closers < openers, can add closer

        var res = new List<string>();
        Helper(n, 0, 0, "", res);

        return res;

        void Helper(int n, int openers, int closers, string s, List<string> res) 
        {
            if (openers == n && closers == n)
            {
                res.Add(s);
                return;
            }

            if (openers < n)
            {
                Helper(n, openers + 1, closers, s + "(", res);
            }

            if (closers < openers)
            {
                Helper(n, openers, closers + 1, s + ")", res);
            }
        }
    }
}
