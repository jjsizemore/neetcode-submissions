public class Solution {
    public int FindMin(int[] nums) {
        // If l > r, shift window right, otherwise left

        int l = 0;
        int r = nums.Length - 1;
        int res = nums[0];

        while (l <= r)
        {
            if (nums[l] <= nums[r])
            {
                res = Math.Min(res, nums[l]);
                break;
            }

            int m = (r - l) / 2 + l;

            if (nums[m] >= nums[l])
            {
                res = Math.Min(res, nums[l]);
                l = m + 1;
            }
            else
            {
                res = Math.Min(res, nums[m]);
                r = m - 1;
            }
        }
        return res;
    }
}
