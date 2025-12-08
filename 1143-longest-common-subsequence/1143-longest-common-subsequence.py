class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def lcs(i: int, j: int, memo: dict = {}) -> int:

            if i == len(text1) or j == len(text2):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            lcs_length = 0

            if text1[i] == text2[j]:
                lcs_length = max(lcs_length, 1 + lcs(i+1, j+1, memo))
            else:
                lcs_length = max(lcs(i+1, j, memo), lcs(i, j+1, memo))
            
            memo[(i,j)] = lcs_length
            
            return lcs_length
        
        return lcs(0,0, {})
        