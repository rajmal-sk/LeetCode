class Solution:


    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        visited = [False] * n
        adj = defaultdict(list)
        s = list(s) # O(N)

        def dfs(i, characters, indices):
            visited[i] = True
            characters.append(s[i])
            indices.append(i)
            for neighbor in adj[i]:
                if not visited[neighbor]:
                    dfs(neighbor, characters, indices)

        # Build the adjacency List
        for src, dst in pairs: # O(E)
            adj[src].append(dst)
            adj[dst].append(src)
        
        for i in range(n):
            if not visited[i]:
                characters = []
                indices = []
                
                dfs(i, characters, indices)
                characters.sort()
                indices.sort()
                for idx, ch in zip(indices, characters):
                    s[idx] = ch
        
        return "".join(s)
    
        