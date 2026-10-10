class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                cur = num
                while cur in numSet:
                    cur += 1
                longest = max(cur - num, longest)
            
        return longest
