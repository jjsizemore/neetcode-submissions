class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            res = max(res, (r - l) * min(heights[l], heights[r]))

            # move the pointer at the smaller height because we're trying to find the maximal area which is limited by the smaller of the two heights
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
        