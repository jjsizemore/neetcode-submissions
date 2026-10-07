public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        // Create a stack with [temp, idx] pairs
        // Iterate through array, while stack.Count > 0 && cur > stack.Peek()[0],
        //  set the val for res at idx from top of stack to cur idx - top idx
        // push [curTemp, curIdx] to top of stack

        var res = new int[temperatures.Length];

        var stack = new Stack<int[]>();

        for (int i = 0; i < res.Length; i++)
        {
            int curTemp = temperatures[i];

            while (stack.Count > 0 && curTemp > stack.Peek()[0])
            {
                int prevDay = stack.Pop()[1];
                res[prevDay] = i - prevDay;
            }

            stack.Push(new int[]{curTemp, i});
        }
        return res;
    }
}
