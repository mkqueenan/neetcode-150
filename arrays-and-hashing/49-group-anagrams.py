class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        anagrams_ = {}
        for s in strs:
            k = sum(ord(char.lower()) for char in s)
            if anagrams_.get(k) is None:
                anagrams_[k] = [s]
            else:
                sublist_ = anagrams_[k]
                sublist_.append(s)
        return [sublist_ for sublist_ in anagrams_.values()]
