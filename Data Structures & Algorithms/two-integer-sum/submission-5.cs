public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var seen = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {
            int cur = nums[i];
            int compl = target - cur;

            if (seen.ContainsKey(compl)) {
                return new int[]{ seen[compl], i };
            }

            seen.TryAdd(cur, i);
        }
        return null;
    }
}

// Space O(n)
// Time O(n)