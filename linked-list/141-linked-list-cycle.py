class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        seen_ = {head}
        curr = head
        while curr:
            curr = curr.next
            if curr not in seen_: seen_.add(curr)
            else: return True
        return False
