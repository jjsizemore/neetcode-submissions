class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '*', '/'])

        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                res = 0

                if t == '+':
                    res = val1 + val2
                elif t == '-':
                    res = val1 - val2
                elif t == '*':
                    res = val1 * val2
                elif t == '/':
                    res = val1 / val2

                stack.append(int(res))
        
        return stack[-1]

# 12