from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source BFS through fruits, starting at 2's
        # scan through grid
        #   add 2s to q (sources)
        #   count fresh fruits -- allows for short circuiting & impossible states
        # Each round of going through grid is 1 minute added to increment

        minTime = 0

        moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        ROWS, COLS = len(grid), len(grid[0])

        # for each 2
        #   update adj 1s -> 2s
        #   decr. freshCount
        #   add new 2 coords to q
        # increment time after each wave
        def bfs(q) -> int:
            time = 0

            nonlocal freshCount
            while q and freshCount > 0:
                wave = len(q)

                for i in range(wave):
                    cur_r, cur_c = q.popleft()

                    for dr, dc in moves:
                        nr, nc = cur_r + dr, cur_c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            freshCount -= 1
                            q.append((nr, nc))
                time += 1

            return -1 if freshCount else time

        q = deque()
        freshCount = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        return bfs(q)

        # Time  O(m * n)
        # Space O(m * n)
