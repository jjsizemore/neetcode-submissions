class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Iteration
        # Iterate through each nums elem and append the set of subsets that contain that elem
        # Start with [[]]
        res = [[]]

        for n in nums:
            temp = []
            for s in res:
                temp.append(s + [n])
            res.extend(temp)

        return res
