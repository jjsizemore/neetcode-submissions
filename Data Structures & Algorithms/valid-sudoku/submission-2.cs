public class Solution {
    public bool IsValidSudoku(char[][] board) {
        Dictionary<int, HashSet<char>> rows = new();
        Dictionary<int, HashSet<char>> cols = new();
        Dictionary<int, HashSet<char>> sqs = new();
        
        for (int r = 0; r < board.Length; r++) {
            for (int c = 0; c < board[0].Length; c++) {
                char val = board[r][c];
                if (val == '.') continue;

                int sqKey = r / 3 * 3 + c / 3;

                if (rows.TryGetValue(r, out var row) && row.Contains(val)
                    || cols.TryGetValue(c, out var col) && col.Contains(val)
                    || sqs.TryGetValue(sqKey, out var sq) && sq.Contains(val))
                    return false;
                
                rows.TryAdd(r, new HashSet<char>());
                cols.TryAdd(c, new HashSet<char>());
                sqs.TryAdd(sqKey, new HashSet<char>());

                rows[r].Add(val);
                cols[c].Add(val);
                sqs[sqKey].Add(val);
            }
        }
        return true;
    }
}
