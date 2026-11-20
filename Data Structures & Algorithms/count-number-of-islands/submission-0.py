class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Scan through rows and cols
        # Once we hit an island:
        #   increment res
        #   we should DFS for neighboring '1's and make them '0's

        res = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c) -> None:
            # if OOB or already water, do nothing
            if not 0 <= r < rows or not 0 <= c < cols:
                return
            if grid[r][c] == '0':
                return

            adj = (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            )

            grid[r][c] = '0'

            # after setting cur cell to water, dfs on neighbors
            for dr, dc in adj:
                dfs(r + dr, c + dc)
            return
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        return res
        