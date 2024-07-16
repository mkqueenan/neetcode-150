class Solution:
    def compare(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if (r and not s) or (not r and s): return False
        if not s and not r: return True
        if r.val == s.val:
            return True and self.compare(r.left, s.left) and self.compare(r.right, s.right)
        else:
            return False

    def helper(self, node: Optional[TreeNode], other: Optional[TreeNode]) -> bool:
        if not node: return False
        if node.val == other.val:
            return self.compare(node, other) or self.helper(node.left, other) or self.helper(node.right, other)
        return self.helper(node.left, other) or self.helper(node.right, other)

    def is_subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.helper(root, subRoot)
