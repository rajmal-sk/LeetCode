# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], small: int, large: int) -> bool:
            if root is None:
                return True
            if not small < root.val < large:
                return False
            left = dfs(root.left, small, root.val)
            right = dfs(root.right, root.val, large)
            return left and right
        return dfs(root, float('-inf'), float('inf'))
