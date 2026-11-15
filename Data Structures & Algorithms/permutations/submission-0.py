class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # If all nums elems are unique, elems in permutations must also be unique
        # Backtrack w/ recursive helper function
        res = []
        # dfs(taken, perm)
        # will recurse through perms by looping through elems in nums
        # if elem at cur not in taken, append to perm and add to taken
        # recurse with new taken and perm
        # remove elem from perm
        def dfs(taken, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())

        # loop should do the job of grabbing any number @ range(len(nums)) not added to perm
            for cur in range(len(nums)):
                if nums[cur] not in taken:
                    taken.add(nums[cur])
                    perm.append(nums[cur])
                    dfs(taken, perm)

                    # necessary for the skipping part of backtracking -- without this all we get is the original order
                    taken.remove(nums[cur])
                    perm.pop()
        # taken avoids duplicates
        # base case len(taken) == len(nums): res.append(perm.copy())

        dfs(set(), [])

        return res
        # Time O(n * n!)
        # Space O(n)
