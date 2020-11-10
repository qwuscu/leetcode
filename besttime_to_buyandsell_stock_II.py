from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        valley = prices[0]
        peak = prices[0]
        n = len(prices)
        i = 0
        while i < n-1:
            while (i < n-1) and (prices[i] >= prices[i+1]): # need >=, [3,3] infinite loop
                i += 1
            valley = prices[i]
            while (i < n-1) and (prices[i] <= prices[i+1]):
                i += 1
            peak = prices[i]
            ans += peak - valley
        return ans



if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))