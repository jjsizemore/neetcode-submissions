class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = deque()

        for c in s:
            if c in pairs:
                stack.append(c)
                continue
            
            if len(stack) > 0 and pairs[stack[-1]] == c:
                stack.pop()
                continue
            
            return False

        return len(stack) == 0

# Time O(n)
# Space O(n)