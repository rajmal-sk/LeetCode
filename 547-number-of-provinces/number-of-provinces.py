class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()

        # Depth First Search of a Node
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        # Create an adjacency list for traversal
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        

        provinces = 0

        # Iterate over each connected component
        for i in range(n):
            if i not in seen:
                provinces += 1
                seen.add(i)
                dfs(i)

        return provinces
        