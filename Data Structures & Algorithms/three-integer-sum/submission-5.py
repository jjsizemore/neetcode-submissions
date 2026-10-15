class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 pointers, outer loop for i, inner loop for k, find j between them
        # i, j, k implicitly distinct
        # add vals to set of tuples

        valid = set()

        for i in range(len(nums) - 2):
            seen = set()
            for k in range(i + 1, len(nums)):
                if (nums[i] + nums[k]) * -1 in seen:
                    valid.add(tuple(sorted((nums[i], ((nums[i] + nums[k]) * -1), nums[k]))))
                seen.add(nums[k])
        
        return [list(triple) for triple in valid]