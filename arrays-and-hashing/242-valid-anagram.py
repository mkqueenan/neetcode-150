class Solution:
    def valid_anagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        s_ = ''.join(sorted(s.lower()))
        t_ = ''.join(sorted(t.lower()))
        return s_ == t_
