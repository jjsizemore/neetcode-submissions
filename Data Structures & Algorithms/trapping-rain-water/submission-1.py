class Solution:
    def trap(self, height: List[int]) -> int:
        # create two new lists of heights
        # one for max value seen from left, one for right
        # [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
        # [1, 2, 3, ....]
        # iterate through original heights
        # if the height is lower than the min of the l and r arrays, trapped water will be the diff between that min and the actual height

        l_max, r_max = [0] * len(height), [0] * len(height)
        l_max[0] = height[0]
        r_max[-1] = height[-1]
        for i in range(1, len(height)):
            l_max[i] = max(height[i], l_max[i - 1])
            r_max[len(height) - 1 - i] = max(height[len(height) - i - 1], r_max[len(height) - i])

        res = 0
        
        for i in range(len(height)):
            lower_bar = min(l_max[i], r_max[i])
            if height[i] < lower_bar:
                res += (lower_bar - height[i])
        
        return res