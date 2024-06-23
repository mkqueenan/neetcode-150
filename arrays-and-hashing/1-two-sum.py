class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        diffs = {}
        for idx, ele in enumerate(nums):
            difference = target - ele
            diffs[difference] = idx
        for idx, ele in enumerate(nums):
            if ele in diffs:
                if idx != diffs[ele]:
                    return [idx, diffs[ele]]
        return []
