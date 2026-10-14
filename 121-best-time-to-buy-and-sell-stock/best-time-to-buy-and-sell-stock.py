class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # sliding window, but variable length
        # if condition met,increase right pointer, if not increase left pointer
        max_diff = 0
        pleft = 0
        pright = 1 if len(prices)>1 else 0 
        curr_diff = prices[pright]-prices[pleft]
        while pleft < pright:
            max_diff = max(max_diff,curr_diff)

            if prices[pleft] < prices[pright]:
                pright+=1
            else:
                pleft=pright
                pright+=1
            if pright == len(prices):
                return max_diff
            curr_diff = prices[pright] - prices[pleft] 
        return max_diff
