public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        
        int top = 0;
        int bot = rows - 1;
        int row = 0;
        while (top <= bot)
        {
            row = (bot - top / 2 + top);

            if (matrix[row][cols - 1] < target)
            {
                top = row + 1;
            }
            else if (matrix[row][0] > target)
            {
                bot = row - 1;
            }
            else
            {
                break;
            }
        }

        if (top > bot) return false;

        int l = 0;
        int r = cols - 1;
        while (l <= r)
        {
            int m = (r - l) / 2 + l;

            if (matrix[row][m] == target)
            {
                return true;
            }
            else if (matrix[row][m] > target)
            {
                r = m - 1;
            }
            else
            {
                l = m + 1;
            }
        }
        return false;
    }
}
