class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Hash Set Backtracking Solution
        # place queens row by row from top
        # track taken cols, posDiags, and negDiags in hash sets
        # at each row, iterate through the row
        # for a spot board[r][c]
        #   if no Q in col, negDiag, or posDiag 
        #       choose (r,c)
        #       add c to cols, r + c to posDiag, r - c to negDiag
        #       recurse into next row
        #       unchoose (r,c) and remove from sets
    
        # base case r == n, append row list to res

        board = [['.'] * n for _ in range(n)]

        res = []

        col = set()
        posDiag = set()
        negDiag = set()

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c not in col and r+c not in posDiag and r-c not in negDiag:
                    # choose space & track attacked places
                    board[r][c] = 'Q'
                    col.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    # recurse into next row
                    dfs(r+1)
                    # unchoose
                    board[r][c] = '.'
                    col.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)

        dfs(0)
        return res
        # Time  O(n! * n)
        #   n! paths
        #   inner loop cost n
        #   n^2 work at each valid soln, but far fewer solns than paths
        # Space O(n^2)
        #   n^2 space for the board