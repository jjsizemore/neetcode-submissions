public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        // Since all the rows are sorted, we can treat the entire matrix like one big array
        // This allows us to run BST in one pass

        int l = 0, r = matrix.Length * matrix[0].Length - 1;

        while (l <= r)
        {
            int middle = (r - l) / 2 + l;

            int row = middle / matrix[0].Length;
            int col = middle % matrix[0].Length;

            int cur = matrix[row][col];

            if (cur == target)
            {
                return true;
            }
            else if (cur < target)
            {
                l = middle + 1;
            }
            else
            {
                r = middle - 1;
            }
        }

        return false;
    }
}
