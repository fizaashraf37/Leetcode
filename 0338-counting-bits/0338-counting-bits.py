class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = [0,1,1,2]
        bits_range = 4

        while len(ans) < n+1:
            for i in range(bits_range):
                ans.append(ans[i]+1)
            bits_range = bits_range << 1
            
        return ans[0:n+1]

        