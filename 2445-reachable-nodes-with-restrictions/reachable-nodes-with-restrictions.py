class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        rest = set(restricted)
        graph = defaultdict(list)
        seen = set()
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        def dfs(node):
            for node in graph[node]:
                if node not in seen and node not in rest:
                    seen.add(node)
                    dfs(node)
        seen.add(0)
        dfs(0)
        return len(seen)