from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    
    # Edge case if invalid input
    # is provided.
    if not prices:
        return 0

    '''
    An interesting approach necessary for the
    two-transaction variant.
    You can solve this in reverse with mirrored logic!
    '''
    max_profit = 0 # For exchanges made from the right.
    peak = float('-inf')
    for i in reversed(range(len(prices))):
        max_profit = max(max_profit, peak - prices[i])
        peak = max(prices[i], peak)
    return max_profit    
    
    '''
    Keep track of the maximum profit so far.
    Scan through and compute the difference
    between the valley of the chart and the
    current price.
    '''
    max_profit = 0
    valley = float('inf')
    for price in prices:
        max_profit = max(max_profit, price - valley)
        valley = min(valley, price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
