class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const unique = new Set(nums);

        if (unique.size < nums.length)
            return true;
        return false;
    }
}
