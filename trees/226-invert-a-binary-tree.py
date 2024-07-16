class Solution:
    def helper(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node: return None
        node.left, node.right = self.helper(node.right), self.helper(node.left)
        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root)
