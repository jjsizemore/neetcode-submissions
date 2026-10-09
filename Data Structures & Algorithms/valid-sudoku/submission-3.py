class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == '.':
                    continue

                if cur in rows[r]:
                    return False
                else:
                    rows[r].add(cur)
                
                if cur in cols[c]:
                    return False
                else:
                    cols[c].add(cur)
                
                squareIdx = (r // 3) * 3 + (c // 3)
                if cur in squares[squareIdx]:
                    return False
                else:
                    squares[squareIdx].add(cur)
        
        return True

# Time O(N^2)
# Space O(N^2)
