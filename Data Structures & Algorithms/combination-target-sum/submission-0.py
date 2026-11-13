class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Backtracking DFS

        res = []
        perm = []
        
        # recurse through list trying diff combos
        # base cases:   sum(perm) > target return
        #               sum(perm) == target res.append(perm)
        # avoid duplicates by only trying starting at current idx
        def dfs(i, curSum):
            if i == len(nums) or sum(perm) > target:
                return
            if curSum == target:
                res.append(perm.copy())
                return

            perm.append(nums[i])
            # 2 branches: 
            # - incl. nums[i] and stay @ i
            # - skip nums[i] without adding it
            dfs(i, curSum + nums[i])
            perm.pop()
            dfs(i + 1, curSum)

        dfs(0, 0)
        return res