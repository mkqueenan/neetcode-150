class Solution:
    def max_area(self, heights: List[int]) -> int:
        if not heights:
            return 0
        left, right = 0, 1
        max_area = 0
        while left < len(heights) - 1:
            while right < len(heights):
                curr_height = min(heights[left], heights[right])
                curr_length = abs((left - right))
                max_area = max((curr_height * curr_length), max_area)
                right += 1
            left += 1
            right = left + 1
        return max_area
