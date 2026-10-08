class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let seen: Map<number, number> = new Map<number, number>();

        for (let i: number = 0; i < nums.length; i++) {
            const cur: number = nums[i];
            const compl: number = target - cur;

            if (seen.has(compl)) return [seen.get(compl)!, i];
            seen.set(cur, i);
        }

        return [];
    }
}

// Time O(n)
// Space O(n)
