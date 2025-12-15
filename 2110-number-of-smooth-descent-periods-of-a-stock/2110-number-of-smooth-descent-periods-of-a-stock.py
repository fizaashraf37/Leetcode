class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        count = len(prices)
        n = 0

        for i in range(len(prices)):
            if i > 0 and prices[i-1] - prices[i] != 1:
                count += (n*(n-1))//2
                n = 0
            n += 1
        
        count += (n*(n-1))//2

        return count


        