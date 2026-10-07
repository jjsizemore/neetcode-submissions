public class Solution {
    public int Search(int[] nums, int target) {
        // Bin Search using l & r ptrs
        // If cur < target, l = mid + 1

        int l = 0, r = nums.Length - 1;

        while (l <= r)
        {
            int mid = ((r - l) / 2) + l;

            if (nums[mid] == target)
                return mid;
            else if (nums[mid] > target)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return -1;
    }
}
