class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '*', '/'])

        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(t)
            else:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                res = 0

                if t == '+':
                    res = val1 + val2
                elif t == '-':
                    res = val1 - val2
                elif t == '*':
                    res = val1 * val2
                elif t == '/':
                    fac1 = 1
                    fac2 = 1
                    if val1 < 0:
                        fac1 = -1
                    if val2 < 0:
                        fac2 = -1
                    res = (val1 * fac1) // (val2 * fac2) * fac1 * fac2

                stack.append(res)
        
        return int(stack[-1])

# 12