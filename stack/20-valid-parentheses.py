def matching(open_: str, close_: str) -> bool:
    pairs_ = {'(': ')', '{': '}', '[': ']'}
    matching_ = pairs_.get(open_, None)
    return matching_ == close_


def isValid( s: str) -> bool:
    if not s:
        return False
    open_ = {'(', '{', '['}
    valid_ = []
    for char in s:
        if char in open_:
            valid_.append(char)
        else:
            try:
                last_ = valid_.pop()
                if matching(last_, char):
                    continue
                else:
                    return False
            except IndexError:
                return False
    return not valid_
