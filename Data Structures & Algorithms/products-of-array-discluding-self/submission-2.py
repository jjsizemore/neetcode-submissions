class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for idx in range(1, len(nums)):
            prefix[idx] = prefix[idx - 1] * nums[idx - 1]
            suffix[len(nums) - 1 - idx] = suffix[len(nums) - idx] * nums[len(nums) - idx]
        
        return [prefix[i] * suffix[i] for i in range(len(nums))]

