class Solution:
    def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if (p and not q) or (not p and q): return False
        if p.val == q.val:
            return self.helper(q.left, p.left) and self.helper(q.right, p.right)
        else:
            return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)
