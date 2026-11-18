class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate through squares, backtrack choose squares around them
        # 
        # base case cur elem is not target char
        # base case cur elem is target char & len(visited) == len(word)
        # 
        # each recursion level should be next val in word, word[idx]
        # helper method should take in row, col, wordIdx
        # mutate elem to '#' before recursing, undo on backtrack

        moves = [
            (1, 0),     # 1 row down
            (-1, 0),    # 1 row up
            (0, -1),    # 1 col left
            (0, 1)      # 1 col right
        ]

        rows = len(board)
        cols = len(board[0])

        # check cur rowc
        def dfs(r, c, wordIdx):
            if (
                    not (0 <= r < rows) or 
                    not (0 <= c < cols) or 
                    board[r][c] == '#' or 
                    board[r][c] != word[wordIdx]
                ):
                return False

            if wordIdx == len(word) - 1:
                return True
        

            board[r][c] = '#'

            for dr, dc in moves:
                if dfs(r + dr, c + dc, wordIdx + 1):
                    return True
            
            board[r][c] = word[wordIdx]
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False

        # m = rows
        # n = cols
        # L = len(word)
        # Time O(m * n * 4^L) 
        #   m * n cells as potential starts
        #   4^L -> 4 branches for each of L recurses

        # Space O(L) recursion depth
