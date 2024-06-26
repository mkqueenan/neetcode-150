class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        left, right, max_len = 0, 1, 1
        chars_ = set(s[left])
        while right < len(s):
            if s[right] not in chars_:
                chars_.add(s[right])
                max_len = max(max_len, len(chars_))
                right += 1
            else:
                chars_.clear()
                left += 1
                right = left + 1
                chars_.add(s[left])
        return max_len
