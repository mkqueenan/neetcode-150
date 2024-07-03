class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2: return list2
        if list1 and not list2: return list1
        if not list1 and not list2: return None
        q_ = []
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                q_.append(curr1)
                curr1 = curr1.next
            else:
                q_.append(curr2)
                curr2 = curr2.next
        if curr1:
            while curr1:
                q_.append(curr1)
                curr1 = curr1.next
        if curr2:
            while curr2:
                q_.append(curr2)
                curr2 = curr2.next
        new_head = q_[0]
        prev = new_head
        while q_:
            curr = q_.pop(0)
            prev.next = curr
            prev = curr
        return new_head
