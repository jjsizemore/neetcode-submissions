class Solution:
    def calc(self, l: int, r: int, heights: List[int]):
        return (r - l) * min(heights[l], heights[r])

    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = min(heights[l], heights[r]) * (r - l)

        while l < r:
            res = max(res, self.calc(l, r, heights))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
        