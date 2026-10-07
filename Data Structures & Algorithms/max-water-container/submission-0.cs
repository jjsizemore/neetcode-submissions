public class Solution {
    public int MaxArea(int[] heights) {
        int[] maxLeft = new int[heights.Length];
        maxLeft[0] = heights[0];
        for (int i = 1; i < heights.Length; i++) {
            maxLeft[i] = Math.Max(heights[i], maxLeft[i - 1]);
        }
        int res = 0;
        for (int i = heights.Length - 1; i >= 0; i--) {
            for (int j = 0; j < heights.Length; j++) {
                if (j > 0 && maxLeft[j] == maxLeft[j - 1]) continue;

                res = Math.Max(res, Math.Min(heights[i], maxLeft[j]) * (i - j));
            }
        }

        return res;
    }
}
