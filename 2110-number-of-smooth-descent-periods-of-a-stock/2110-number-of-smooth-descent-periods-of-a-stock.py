class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        count = len(prices)
        n = 1

        for i in range(1, len(prices)):
            if prices[i-1] - prices[i] != 1:
                count += (n*(n-1))//2
                n = 0
            n += 1
        
        count += (n*(n-1))//2

        return count


        