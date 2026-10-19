class Solution:
    def trap(self, height: List[int]) -> int:
        # maintain 2 pointers, and track l_max and r_max
        # at each index, the lesser max is the bottleneck
        # if height < min(l_max, r_max), add diff to res and increment the ptr

        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]

        res = 0

        while l < r:
            cur_min = min(l_max, r_max)
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]

        return res
