def characterReplacement(s: str, k: int) -> int:
    if not s:
        return 0
    if len(s) == 1:
        return 1
    left, right, max_len, subs = 0, 1, 0, k
    while right < len(s):
        if s[left] == s[right]:
            curr_len = abs(left - right) + 1
            max_len = max(curr_len, max_len)
            right += 1
        elif subs > 0:
            curr_len = abs(left - right) + 1
            max_len = max(curr_len, max_len)
            right += 1
            subs -= 1
        else:
            subs = k
            left = right - 1
            right = left + 1
    return max_len


s = str(input())
n = int(input())
print(characterReplacement(s, n))