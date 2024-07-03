class Solution:
    def helper(self, curr: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if not curr:
            return prev
        next_ = curr.next
        curr.next = prev
        return self.helper(next_, curr)

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head, None)
