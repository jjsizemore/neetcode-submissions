public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        
        int top = 0;
        int bot = rows - 1;
        int mid = 0;
        while (top <= bot)
        {
            mid = (bot - top / 2 + top);

            if (matrix[mid][cols - 1] < target)
            {
                top = mid + 1;
            }
            else if (matrix[mid][0] > target)
            {
                bot = mid - 1;
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

            if (matrix[mid][m] == target)
            {
                return true;
            }
            else if (matrix[mid][m] > target)
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
