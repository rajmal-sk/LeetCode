# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []    
        q = deque([root] if root else [])
        dir = 1 # left to right

        while q:
            n = len(q)
            clevel = []
            for i in range(n):
                if dir:
                    node = q.popleft()
                    clevel.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    node = q.pop()
                    clevel.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
            res.append(clevel)
            dir = 1 - dir
        return res
                