class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS from border cells w/ hash sets tracking cells with non-decreasing paths to them

        pac = set()
        atl = set()

        ROWS, COLS = len(heights), len(heights[0])
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []
        # search in from border set of cells
        # if neighboring cell is valid, recurse on it
        # at each recurse, add coord to validSet
        def dfs(r, c, validSet) -> None:
            # invariant: any cell is validSet is fully explored
            validSet.add((r, c))

            # looping through neighbors means continue rather than return on invalid cells
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < ROWS or not 0 <= nc < COLS:
                    continue
                if heights[nr][nc] >= heights[r][c] and (nr, nc) not in validSet:
                    dfs(nr, nc, validSet)


        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

        # Time  O(m * n)
        # Space O(m * n)