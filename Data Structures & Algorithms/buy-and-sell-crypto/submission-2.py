class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_prof = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            max_prof = max(prices[r] - prices[l],max_prof)

        return max_prof