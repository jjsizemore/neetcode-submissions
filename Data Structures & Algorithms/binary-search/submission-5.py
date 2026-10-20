class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # sorted means we can use binary search
        # two pointers l & r, start at ends, and while l < r
        # find middle idx, if val is larger than target, r becomes middle - 1
        # else l becomes middle

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            val = nums[mid]
            if val > target:
                r = mid - 1
            elif val == target:
                return mid
            else:
                l = mid + 1
        
        return -1