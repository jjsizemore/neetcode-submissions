public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        // Can use a stack to keep track of the farthest up car in each fleet
        // As we iterate through cars, if car at top of stack reaches cur car
        // pop top
        // Stack values will be time to target
        // while curTime >= stack.Peek(), pop
        // Num fleets is num times

        var stack = new Stack<double>();
        int n = position.Length;
        var pairs = new int[n][];

        for (int x = 0; x < n; x++)
        {
            pairs[x] = new int[]{ position[x], speed[x] };
        }

        Array.Sort(pairs, (a, b) => a[0] - b[0]);

        foreach (var p in pairs)
        {
            double t = (double)(target - p[0]) / p[1];

            while (stack.Count > 0 && stack.Peek() <= t)
            {
                stack.Pop();
            }
            stack.Push(t);
        }

        return stack.Count;
    }
}
