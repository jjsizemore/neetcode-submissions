class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking 
        res = []
        # holds current subset we're building
        # each subset built out recursively via DFS
        subset = []

        # recurses through the indices with & without
        # the elem at i in nums
        # base case i == len(nums); append subset to res
        def dfs(i):
            if i == len(nums):
                # copy so we're not manipulating same list whole time
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)


        dfs(0)
        return res
