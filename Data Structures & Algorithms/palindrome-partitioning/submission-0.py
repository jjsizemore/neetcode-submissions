class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # "every" means a sequence of decisions, 1 per substring, all must succeed
        # find "all" means cut the string from the left, 1 palindrome at a time
        # when does the first piece end?
        #   
        # "aab"                 "aab"
        #   |   \                 |  
        #  "a"   (skip)          "aa"
        #   |                      |
        #  "a"                     "b"
        #   |
        #  "b"
        #   |
        # ["a", "a", "b"]
        # pick where the first substring ends and recurse on the rest
        # 
        # recursive function part(i)
        # i = start of the rest of the string after chosen substrings
        # iterate through i -> len(s) - 1
        # for each substring s[i:j+1], is it a pali?
        # if yes, append & recurse with i = j + 1
        # pop after, to backtrack

        part = []
        res = []

        def isPalindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            # base case: no chars left -> found valid partition
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                sub = s[i:j+1]

                if isPalindrome(i, j):
                    part.append(sub)
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res

        # Time  O(n * 2^n) 
        #   there are n-1 decisions, cut or don't cut
        #   each decision does O(n) work for isPalindrome
        #   
        # Space O(n)
        #   stack depth max n
