class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Iteration
        # Iterate through each nums elem and append the set of subsets that contain that elem
        # Start with [[]]
        res = [[]]

        for num in nums:
            temp = []
            for s in res:
                temp.append(s + [num])
            res.extend(temp)

        return res

    # Time O(n * 2^n) 2^n sets, each requiring a copy that costs n