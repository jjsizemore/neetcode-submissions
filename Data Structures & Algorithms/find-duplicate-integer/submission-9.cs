public class Solution {
    public int FindDuplicate(int[] nums) {
        // Marking the numbers as seen in place
        // Since the indices of the array are generally 1:1 with the numbers, can use the indices to mark seen numbers in place

        // Step 1: Iterate through whole array
        for (int i = 0; i < nums.Length; i++)
        {
            int curNum = Math.Abs(nums[i]);
            // Step 2: Check if index assoc. w/ cur number has been seen
            if (nums[curNum - 1] < 0)
            {
                // Step 3.a: Return the seen number
                return curNum;
            }
            else
            {
                // Step 3.b: Mark the number's index as seen
                nums[curNum - 1] *= -1;
            }
        }
        return -1;
    }
}
