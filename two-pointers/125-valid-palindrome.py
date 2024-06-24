class Solution:
    def is_palindrome(self, s: str) -> bool:
        if not s:
            return False
        if len(s) == 1:
            return True
        str_ = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        head, tail = 0, len(str_) - 1
        while head < tail:
            if str_[head] == str_[tail]:
                head += 1
                tail -= 1
            else:
                return False
        return True
