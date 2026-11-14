class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Backtrack DFS
        # define helper dfs(i, curSum)
        # helper will recurse through indices
        # add num[i] to a perm, recurse on i + 1
        # pop num[i] and recurse on i + 1
        # base cases:
        #  - curSum == target: append to res & return
        #  - curSum > target or i == len(candidates): return
        res = []
        perm = []

        candidates.sort()

        def dfs(i, curSum) -> None:
            if curSum == target:
                res.append(perm.copy())
                return
            if curSum > target or i == len(candidates):
                return

            perm.append(candidates[i])
            dfs(i + 1, curSum + candidates[i])
            perm.pop()
            j = i + 1
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1    
            dfs(j, curSum)

        dfs(0, 0)
        return res
