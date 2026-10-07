public class Solution {
    public int Trap(int[] height) {
        int area = 0, l = 0, r = height.Length - 1;
        int[] lMax = new int[height.Length];
        int[] rMax = new int[height.Length];
        lMax[0] = height[0];
        rMax[height.Length - 1] = height[height.Length - 1];

        for (int i = 1; i < height.Length; i++) {
            lMax[i] = Math.Max(lMax[i - 1], height[i]);
            rMax[height.Length - 1 - i] = Math.Max(rMax[height.Length - i], height[height.Length - 1 - i]);
        }

        for (int i = 1; i < height.Length; i++) {
            area += Math.Min(lMax[i], rMax[i]) - height[i];
        }

        return area;
    }
}
