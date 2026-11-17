class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # can only close an open parenthesis
        res = []

        # o = # opening parentheses
        # c = # closing parentheses
        # cur = current string
        # 
        def dfs(o: int, c: int, cur: List[str]) -> None:
            if c > o or o > n or c > n:
                return
            if len(cur) == 2*n:
                res.append(''.join(cur))
                return

            cur.append('(')
            o += 1
            dfs(o, c, cur)
            cur.pop()
            o -= 1

            cur.append(')')
            c += 1
            dfs(o, c, cur)
            cur.pop()
            c -= 1
        
        dfs(0, 0, [])

        return res