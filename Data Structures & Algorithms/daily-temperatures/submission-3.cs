public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        // Can use monotonically decreasing stack of [temp, idx]
        // Whenever curTemp > stack.Peek()[0], pop and set res[idx] to curIdx - idx
        // Values that aren't set at the end will just be 0s

        int n = temperatures.Length;
        var res = new int[n];
        var stack = new Stack<int[]>();

        for (int i = 0; i < n; i++)
        {
            while (stack.Count > 0 && stack.Peek()[0] < temperatures[i])
            {
                int oldIdx = stack.Pop()[1];
                res[oldIdx] = i - oldIdx;
            }
            stack.Push(new int[]{temperatures[i], i});
        }

        return res;
    }
}
