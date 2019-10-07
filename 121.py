from typing import List


# time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_cost = prices[0]
        # max_sold = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            min_cost = min(min_cost, prices[i])
            # max_sold = max(max_sold, prices[i])
            max_profit = max(max_profit, prices[i] - min_cost)
        return max_profit

if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
