class Solution:
    def max_profit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        left, right, max_diff = 0, 1, 0
        while right < len(prices):
            if prices[left] < prices[right]:
                curr_diff = prices[right] - prices[left]
                max_diff = max(max_diff, curr_diff)
                right += 1
            else:
                left += 1
                right = left + 1
        return max_diff
