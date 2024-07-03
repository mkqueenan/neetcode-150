class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> None:
        if not head: return None
        if head.next == None: return head

        all_ = [head]
        curr = head.next
        while curr:
            all_.append(curr)
            curr = curr.next

        mid = len(all_) // 2
        left_, right_ = all_[:mid], all_[mid:][::-1]

        for idx, node in enumerate(left_):
            node.next = right_[idx]
        for idx, node in enumerate(right_):
            try:
                node.next = left_[idx + 1]
            except IndexError:
                if idx < len(right_) - 1:
                    node.next = right_[idx + 1]
                else:
                    node.next = None
        return left_[0]
