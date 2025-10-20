class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Edge Case: Source == Destination
        if source == destination:
            return True

        graph = defaultdict(list)
       # Generate adjacency list representation of the graph from the edges 
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        ans = False
        def dfs(node):
            nonlocal ans
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if neighbor == destination:
                        ans = True
                        return
                    dfs(neighbor)
        
        seen = {source}
        dfs(source)
        return ans