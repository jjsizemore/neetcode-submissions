public class Solution {
    public bool IsValidSudoku(char[][] board) {
        // Iterate through the diagonal cells, checking that the row and col that each belong to are valid
        // Iterate through each 3x3 sub-box, checking that they're valid
        // Perform validity check by creating set & if value is not '.' and already present, return false
        Dictionary<int, HashSet<char>> cols = new();
        Dictionary<int, HashSet<char>> rows = new();
        Dictionary<int, HashSet<char>> squares = new();
    
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                char val = board[i][j];
                if (val == '.') continue;

                if (rows.TryGetValue(i, out var rowSet) && rowSet.Contains(val)
                    || cols.TryGetValue(j, out var colSet) && colSet.Contains(val)
                    || squares.TryGetValue(i / 3 * 3 + j / 3, out var squareSet) && squareSet.Contains(val))
                {
                    return false;
                }
                cols.TryAdd(j, new HashSet<char>());
                rows.TryAdd(i, new HashSet<char>());
                squares.TryAdd(i / 3 * 3 + j / 3, new HashSet<char>());
                cols[j].Add(val);
                rows[i].Add(val);
                squares[i / 3 * 3 + j / 3].Add(val);
            }
        }
        return true;
    }
}
