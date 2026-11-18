class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # each number is a decision between the letters it's connected to
        # finding all possible combos requires backtracking
        # each number is a recursion level
        # at each recursion level, loop through the chars for a num, choose, explore, unchoose
        # if recursion has run through all nums, append the combo
        # state to track is:
        #   index of digits string
        #   combo

        if not digits:
            return []
        res = []

        toChar = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }

        combo = []
        def dfs(i):
            if i == len(digits):
                res.append(''.join(combo))
                return
            
            for c in toChar[digits[i]]:
                combo.append(c)
                dfs(i+1)
                combo.pop()
        
        dfs(0)

        return res

