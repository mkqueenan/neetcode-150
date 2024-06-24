import heapq

class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        heap_, links_ = [], {}
        for idx, num in enumerate(nums):
            if links_.get(num) is None:
                links_[num] = (idx, num)
                heapq.heappush(heap_, (num, idx))
        max_length, curr_length = 0, 0
        while heap_:
            curr_length += 1
            curr_num, curr_idx = heapq.heappop(heap_)
            if links_.get(curr_num + 1) is None:
                max_length = max(max_length, curr_length)
                curr_length = 0
        return max_length
