class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        prev_row = [0]*(len(text2)+1)
        cur_row = [0]*(len(text2)+1)
        
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    cur_row[j] = prev_row[j-1]+1
                else:
                    cur_row[j] = max(prev_row[j], cur_row[j-1])
            
            prev_row, cur_row = cur_row, prev_row
        
        return prev_row[-1]
        
        #   a b c d e a c
        # a 1 1 1 1 1 1 1
        # c 1 1 2 2 2 2 2
        # e 1 1 2 2 3