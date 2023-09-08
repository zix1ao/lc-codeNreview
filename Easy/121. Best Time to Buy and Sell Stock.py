"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
  ·1 <= prices.length <= 10^5
  ·0 <= prices[i] <= 10^4
"""


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        """
        :param prices: [int]
        :return: int
        """

        """
        This problem is quite simple. It ask us to calculate the
        maximum profit we can achieve through buying stock at the
        lowest and selling at the highest price in the future.
        We first initialize the profit to 0 and buy at 1st day,
        then for the prices in the rest of the day, we compare it
        to our buying price. If our buying price is lower, then we
        calculate the profit by using max function to choose from
        current profit and the difference of current price and our
        buying price. Otherwise, we set our buying price to current
        price. 
        """

        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            if buy < price:
                profit = max(profit, price - buy)
            else:
                buy = price

        return profit



if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))