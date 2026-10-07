public class Solution {
    public int MaxArea(int[] heights) {
        int l = 0, r = heights.Length - 1, area = 0;

        while (l < r) {
            int h = Math.Min(heights[l], heights[r]);

            area = Math.Max(area, h * (r - l));

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return area;
    }
}
