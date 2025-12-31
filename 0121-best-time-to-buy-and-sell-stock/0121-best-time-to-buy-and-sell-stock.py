class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        start = 0
        max_profit = 0

        for end in range(len(prices)):
            cur_profit = prices[end] - prices[start]
            if cur_profit < 0:
                start = end
            max_profit = max(cur_profit, max_profit)
        
        return max_profit


        