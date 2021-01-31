from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(self, prices: List[int]) -> int:
    '''
    1. brute force
    Time complexity
    1. if statement => n * (n - 1)
    2. max => n^2
    Space complexity : O(1) Only max_price used.
    '''
    max_price = 0
    for i, price in enumerate( prices ):
        for j in range( i, len( prices ) ):
            max_price = max( prices[j] - price, max_price )
    return max_price

