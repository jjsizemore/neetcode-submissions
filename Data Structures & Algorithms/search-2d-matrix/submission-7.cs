public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        // Binary search for correct row, then look in row for target
        // If start of row at middle > target, r = middle

        int t = 0;
        int b = matrix.Length - 1;
        int cols = matrix[0].Length;
        bool valid = false;
        
        while (t <= b)
        {
            int middle = (b - t) / 2 + t;
            int cur = matrix[middle][0];

            if (cur > target)
            {
                b = middle - 1;
            }
            else if (cur <= target && target <= matrix[middle][cols - 1])
            {
                t = middle;
                valid = true;
                break;
            }
            else
            {
                t = middle + 1;
            }
        }


        int l = 0, r = cols - 1;
    
        while (valid && l <= r)
        {
            var row = matrix[t];

            int middle = (r - l) / 2 + l;

            if (row[middle] == target)
            {
                return true;
            }
            else if (row[middle] < target)
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
