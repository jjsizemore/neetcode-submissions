public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        // Binary search rows then columns in row that target would likely be in
        // Finding row: target >= row[0] && target<= row[n - 1]

        int m = matrix.Length, n = matrix[0].Length;

        int t = 0, l = 0, b = m - 1, r = n - 1;

        int row = 0;

        while (t <= b)
        {
            row = (b - t) / 2 + t;

            if (target > matrix[row][r])
            {
                t = row + 1;
            } 
            else if (target < matrix[row][0])
            {
                b = row - 1;
            }
            else
            {
                break;
            }
        }
        Console.WriteLine($"r={r}\nm={m}");
        if (t > b) return false;

        while (l <= r)
        {
            int col = (r - l) / 2 + l;

            if (target == matrix[row][col])
            {
                return true;
            }
            else if (target < matrix[row][col])
            {
                r = col - 1;
            }
            else
            {
                l = col + 1;
            }
        }

        return false;
    }
}
