class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        # 2 ptrs, while l < r check sum, if < target, l += 1, else r -= 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [ l + 1, r + 1 ]
            elif curSum < target:
                l += 1
            else:
                r -= 1
        return []

# Time O(n)
# Space O(1)