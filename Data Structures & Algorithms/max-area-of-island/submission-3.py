class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Similar logic to counting islands
        # Scan grid and run dfs when cell is 1
        # Inside dfs:
        #   Change cell to 0 and return 1 + sum of dfs(r + dr, c + dc)
        # In main method, maxArea = max(maxArea, dfs(r, c))
        # return maxArea
        # Only have to track current cell, visited are changed to 0, area is passed up recursion stack

        maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])

        moves = (
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        )

        # instantiate area counter, add the start cell to a stack, and iterate on the stack
        # iterations mean setting cell to 0, incrementing cur area, and adding adjacent land cells to stack
        # after stack is cleared out, recalc maxArea
        def dfs(r, c) -> int:
            curArea = 0
            grid[r][c] = 0
            stack = [(r, c)]

            while stack:
                
                cur_r, cur_c = stack.pop()
                curArea += 1

                for dr, dc in moves:
                    nr = cur_r + dr
                    nc = cur_c + dc

                    if not 0 <= nr < ROWS or not 0 <= nc < COLS:
                        continue
                    if grid[nr][nc] == 0:
                        continue

                    grid[nr][nc] = 0
                    stack.append((nr, nc))

            return curArea

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
            
