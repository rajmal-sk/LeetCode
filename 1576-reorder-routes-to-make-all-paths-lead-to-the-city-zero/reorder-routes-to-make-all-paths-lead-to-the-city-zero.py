class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ugraph = defaultdict(list)
        edges = set()
        # Generate undirected graph from the given directed graph for traversal
        for v1, v2 in connections:
            edges.add((v1, v2))
            ugraph[v1].append(v2)
            ugraph[v2].append(v1)

        
        # Start from 0 and do Depth First Traversal
        def dfs(node):
            ans = 0
            for neighbor in ugraph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    # Checking if edges away from 0 is part of the directed graph
                    if (node, neighbor) in edges:
                        ans += 1
                    ans += dfs(neighbor)
            return ans
        
        seen = {0}
        return dfs(0)
