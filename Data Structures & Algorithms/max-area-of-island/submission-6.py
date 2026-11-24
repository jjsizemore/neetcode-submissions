from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        moves = (
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        )

        def bfs(r, c) -> int:
            curArea = 0
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()

                if not 0 <= r < ROWS or not 0 <= c < COLS:
                    continue
                if grid[r][c] == 0:
                    continue

                grid[r][c] = 0
                curArea += 1
                for dr, dc in moves:
                    q.append((r + dr, c + dc))

            return curArea


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(bfs(r, c), maxArea)

        return maxArea

        # Time  O(m * n) - if all land
        # Space O(m * n) - if stack is whole grid bc snake-like island
