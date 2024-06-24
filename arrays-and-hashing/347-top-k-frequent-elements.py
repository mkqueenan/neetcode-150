import heapq

class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        frequency_ = {}
        for i in nums:
            if frequency_.get(i) is None:
                frequency_[i] = 1
            else:
                tally = frequency_[i]
                frequency_[i] = tally + 1
        heap_ = []
        for key in frequency_.keys():
            heapq.heappush(heap_, (-frequency_[key], key))
        return [heapq.heappop(heap_)[1] for _ in range(k)]
