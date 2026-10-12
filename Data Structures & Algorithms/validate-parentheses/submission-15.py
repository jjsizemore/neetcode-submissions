class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False
        
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack

# Time O(n)
# Space O(n)