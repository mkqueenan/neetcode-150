class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        distinct_ = set(nums)
        if len(distinct_) != len(nums):
            return True
        return False
