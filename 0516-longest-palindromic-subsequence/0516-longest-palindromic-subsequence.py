class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def lps(left: int, right: int, memo: dict = {}) -> int:

            if left > right:
                return 0

            if left == right:
                return 1
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            longest = 0
            if s[left] == s[right]:
                longest = lps(left+1, right-1, memo) + 2
            else:
                longest = max(lps(left+1, right, memo), lps(left, right-1, memo))
            
            memo[(left, right)] = longest
            
            return longest

        return lps(0, len(s)-1)
            

    
