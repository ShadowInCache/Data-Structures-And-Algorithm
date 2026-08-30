class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxPrice = 0

        for i in range(1, len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            else:
                maxPrice = max(maxPrice, (prices[i] - minPrice))
        
        return maxPrice