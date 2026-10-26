class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        tb = 0
        max_prof = 0 
        for ts in range(1, n):
            b = prices[tb]
            s = prices[ts]
            if b > s:
                tb = ts
            else:
                max_prof = max(max_prof, s - b)
        return max_prof
            

            

