class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            cur = nums[mid]

            if cur == target:
                return mid
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

        # Time O(log(n))
        # Space O(1)
