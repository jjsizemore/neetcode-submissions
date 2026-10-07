public class Solution {
    int maxLen;
    List<string> res;  
    public List<string> GenerateParenthesis(int n) {
        // If openers is less than n, can add another opener
        // If closers is less than openers, can add another closer
        // Can use backtracking method to add all the possibilities to a list
        // We can just concat a string instead of building a stack with backtracking
        maxLen = n;
        res = new();
        Backtrack(0, 0, "");
        return res;

        void Backtrack(int nOpen, int nClose, string seq) {
            if (nOpen == maxLen && nClose == maxLen) {
                res.Add(seq);
                return;
            }

            if (nOpen < maxLen) {
                Backtrack(nOpen + 1, nClose, seq + "(");
            }
            if (nClose < nOpen) {
                Backtrack(nOpen, nClose + 1, seq + ")");
            }
        }
    }
}
