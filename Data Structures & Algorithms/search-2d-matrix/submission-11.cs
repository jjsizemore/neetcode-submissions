public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        // Binary search for correct row, then look in row for target
        // If start of row at middle > target, r = middle

        int t = 0;
        int b = matrix.Length - 1;
        int l = 0;
        int r = matrix[0].Length - 1;
        bool valid = false;
        
        while (t <= b)
        {
            int middle = (b - t) / 2 + t;
            int curStart = matrix[middle][l];
            int curEnd = matrix[middle][r];
            
            if (curStart <= target && target <= curEnd)
            {
                t = middle;
                valid = true;
                break;
            }
            else if (curStart > target)
            {
                b = middle - 1;
            }
            else
            {
                t = middle + 1;
            }
        }
    
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
