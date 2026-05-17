class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        min_price = math.inf

        for price in prices:
            if price<min_price:
                min_price=price
            
            profit = price-min_price
            m = max(m,profit)
        return m