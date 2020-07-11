from typing import List
from buy_and_sell_stock import buy_and_sell_stock_once

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:

    '''
    O(n) approach. Uses O(n) space.
    Do one pass through, and for each i,
    record the max_profit attainable if
    the window ends at i.
    Do one pass in reverse using
    mirrored logic and add the two together.
    '''
    # Left windows.
    max_profit_per_left_window = [0] * len(prices)
    max_profit, valley = 0, float('inf')
    for i, price in enumerate(prices):
        valley = min(price, valley)
        max_profit = max(max_profit, price - valley)
        max_profit_per_left_window[i] = max_profit
    
    peak = float('-inf')
    for i in reversed(range(1, len(prices))):
        peak = max(prices[i], peak)
        two_transaction_sum = peak - prices[i] + max_profit_per_left_window[i - 1]
        max_profit = max(max_profit, two_transaction_sum)
    return max_profit

    '''
    O(n^2) approach. For each index in the chart,
    split the chart on that index into two bins.
    Search left and right bins (linear) for the max
    profit attainable in each. Globally keep track of
    this maximum profit.

    Will time out on very large inputs.
    '''
    max_profit = 0
    for i in range(len(prices)):
        max_profit = max(max_profit, 
            buy_and_sell_stock_once(prices[:i]) +
            buy_and_sell_stock_once(prices[i:]
        ))
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
