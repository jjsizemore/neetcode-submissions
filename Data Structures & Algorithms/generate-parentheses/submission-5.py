class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # can only close an open parenthesis
        res = []

        # o = # opening parentheses
        # c = # closing parentheses
        # cur = current string
        # 
        def dfs(o: int, c: int, cur: List[str]) -> None:
            if len(cur) == 2*n:
                res.append(''.join(cur))
                return

            if o < n:
                cur.append('(')
                dfs(o + 1, c, cur)
                cur.pop()

            if c < o:
                cur.append(')')
                dfs(o, c + 1, cur)
                cur.pop()
        
        dfs(0, 0, [])

        return res