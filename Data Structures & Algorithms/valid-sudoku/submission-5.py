class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == '.':
                    continue
                    
                squareIdx = (r // 3, c // 3)

                if cur in rows[r] or cur in cols[c] or cur in squares[squareIdx]:
                    return False
                else:
                    rows[r].add(cur)
                    cols[c].add(cur)
                    squares[squareIdx].add(cur)
        
        return True

# Time O(N^2)
# Space O(N^2)
