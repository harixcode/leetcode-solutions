"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Approach
pointer d start from day 1
pointer f start from day 2
max_profit counter is updated with profit values as it loop through each element
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    buy_day = 0
    sell_day = 0
    day = 1
    d = 0
    while day < len(prices):
        if prices[d] < prices[day]:
            if prices[day] - prices[d] > max_profit:
                max_profit = prices[day] - prices[d]
                buy_day = d +1
                sell_day = day +1
        else: 
            d = day
        day +=1    
    print(f'Buy on day {buy_day} and sell on day {sell_day} to get profit = {max_profit}')
    return max_profit
    
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))

"""
O(n)
"""