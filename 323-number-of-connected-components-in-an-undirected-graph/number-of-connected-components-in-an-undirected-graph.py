class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        ans = 0

        # DFS of a given node
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        # Created an adjacency list representation of the graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        
        for i in range(n):
            if i not in seen:
                seen.add(i)
                ans += 1
                dfs(i)
        
        return ans