import string

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''
        elif len(strs) == 1:
            return '\0' + strs[0]
        return '\0'.join(word.replace(string.whitespace, '\1') if word != '' else '\2' for word in strs)

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        elif s.startswith('\0'):
            return [s[1::]]
        return [word.replace('\1', ' ') if word != '\2' else '' for word in s.split('\0')]
