class Solution:
    def helper(self, node: Optional[TreeNode]) -> int:
        if not node: return 0
        return max(self.helper(node.left), self.helper(node.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)