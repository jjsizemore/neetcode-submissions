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

        Array.Sort(pairs, (b, a) => a[0] - b[0]);
        Console.WriteLine(pairs);

        foreach (var p in pairs)
        {
            stack.Push((double)(target - p[0]) / p[1]);
            if (stack.Count >= 2 && stack.Peek() <= stack.ElementAt(1)) {
                stack.Pop();
            }        
        }

        return stack.Count;
    }
}
