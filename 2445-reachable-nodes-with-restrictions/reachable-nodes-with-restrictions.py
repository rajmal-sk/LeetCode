class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        seen = [False] * n
        for node in restricted:
            seen[node] = True

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        def dfs(node):
            self.ans += 1
            seen[node] = True
            for node in graph[node]:
                if not seen[node]:
                    seen[node] = True
                    dfs(node)
        self.ans = 0
        dfs(0)
        return self.ans