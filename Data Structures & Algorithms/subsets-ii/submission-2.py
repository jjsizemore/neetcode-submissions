class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # At each recursion depth, only use the first occurrence of a value as the next choice.
        # sort so dupe vals are adjacent
        # allows detecting dupes with nums[next] == nums[next - 1]

        nums.sort()
        
        res = []

        def dfs(idx: int, curSet: List[int]) -> None:
            # every recurse path is a valid subset
            # add copy bc curSet is constantly modified during backtracking
            res.append(curSet.copy())
            
            # try adding each poss. next elem
            for next in range(idx, len(nums)):
                # if val is same as prev. at this recursion depth, skip to avoid duplicates
                # 
                # only skip when next > idx bc first occurrence should still be allowed
                # dupes can still be chosen at a lower lvl, which is necessary for subsets like [1, 1]
                if next > idx and nums[next] == nums[next - 1]:
                    continue

                # choose nums[next]
                curSet.append(nums[next])

                # continue building subset using elems to the right & going down the recurse stack
                dfs(next + 1, curSet)

                # undo the choice before trying next candidate
                # this is how you get subsets that skip 1 or more elems
                curSet.pop()

        dfs(0, [])

        return res
        # Time O(n * 2^n) 2^n paths each requiring a copy that takes O(n)
        # Space O(n) extra space for the curSet
