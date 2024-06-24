from functools import reduce

class Solution:

    def div(self, i, sublist_) -> int:
        return reduce(lambda x, y: x * y, sublist_)

    def product_except_self(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        return [self.div(num, nums[:idx] + nums[idx + 1:]) for idx, num in enumerate(nums)]
