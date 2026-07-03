class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0

        min = None
        max = 0

        for price in prices:

            if min is None or price < min:
                min = price
            elif max is None:
                max = 0
            elif price - min > max:
                max = price - min

        return max