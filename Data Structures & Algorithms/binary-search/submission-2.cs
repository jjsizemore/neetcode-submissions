public class Solution {
    public int Search(int[] nums, int target) {
        int l = 0, r = nums.Length - 1;

        while (l <= r) 
        {
            int mid = ((r - l) / 2) + l;
            int cur = nums[mid];

            if (cur == target)
            {
                return mid;
            }
            else if (cur > target)
            {
                r = mid - 1;
            }
            else
            {
                l = mid + 1;
            }
        }

        return -1;
    }
}
