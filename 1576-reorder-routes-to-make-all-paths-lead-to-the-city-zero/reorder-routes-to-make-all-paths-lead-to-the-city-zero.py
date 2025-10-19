class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ugraph = defaultdict(list)
        edges = set()
        # Generate undirected graph from the given directed graph for traversal
        for v1, v2 in connections:
            edges.add((v1, v2))
            ugraph[v1].append(v2)
            ugraph[v2].append(v1)

        seen = set()
        count = 0
        # Start from 0 and do Depth First Traversal
        def dfs(node):
            nonlocal count
            for neighbor in ugraph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if (node, neighbor) in edges:
                        count += 1
                    dfs(neighbor)
        seen.add(0)
        dfs(0)
        return count
