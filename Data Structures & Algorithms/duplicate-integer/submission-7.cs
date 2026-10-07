public class Solution {
    public bool hasDuplicate(int[] nums) {
        return nums.Length > new HashSet<int>(nums).Count;
    }
}