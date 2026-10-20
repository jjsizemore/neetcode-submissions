class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # if nums[mid] < nums[l], r = mid - 1
        # if nums[r] < nums[mid], l = mid + 1
        min = nums[0]
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r - l) // 2 + l

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[r]