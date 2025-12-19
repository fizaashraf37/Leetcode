class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        return self.lcs(s, s[::-1])

    def lcs(self, s: str, t: str) -> int:

        prev_row = [0]*(len(s)+1)
        cur_row = [0]*(len(s)+1)

        for i in range(1, len(s)+1):
            for j in range(1, len(s)+1):
                if s[i-1] == t[j-1]:
                    cur_row[j] = prev_row[j-1] + 1
                else:
                    cur_row[j] = max(prev_row[j], cur_row[j-1])
            prev_row, cur_row = cur_row, prev_row
        
        return prev_row[-1]


#     a b c d e
#   0 0 0 0 0 0
# a 0 1 1 1 1 1
# c 0 1 1 2 2 2
# g 0 1 1 1 1 1
# e 0
# f 0
