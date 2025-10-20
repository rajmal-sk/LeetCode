# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        tar = target.val
        
        def dfs(root):
            if root is None:
                return 
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        for x in graph:
            print(graph[x])

        seen = {tar}
        queue = deque([(tar, 0)])
        ans= []

        while queue:
            node, depth = queue.popleft()
            if depth == k:
                ans.append(node)
            if depth > k:
                break
            
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))
        
        return ans
