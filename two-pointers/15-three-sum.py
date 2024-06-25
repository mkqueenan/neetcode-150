class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return [[]]

        left, right = 0, 1
        pairs_ = {}
        while left < len(nums) - 1:
            while right < len(nums):
                difference = 0 - sum([nums[left], nums[right]])
                if pairs_.get(difference) is None:
                    pairs_[difference] = [(left, right)]
                else:
                    lst_ = pairs_[difference]
                    lst_.append([left, right])
                right += 1
            left += 1
            right = left + 1

        triplets_ = set()
        for idx, ele in enumerate(nums):
            if ele in pairs_.keys():
                combos_ = pairs_[ele]
                for tuple_ in combos_:
                    if idx not in tuple_:
                        triplets_.add(tuple(sorted([nums[idx], nums[tuple_[0]], nums[tuple_[1]]])))

        return [list(triplet) for triplet in triplets_]
