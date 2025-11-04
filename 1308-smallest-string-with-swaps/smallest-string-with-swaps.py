class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x: int) -> int:
        # Here we are compressing the path
        # Amortized time complexity is alpha(V) - Inverse Ackermann Function
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        xPar = self.find(x) # each find alpha(v)
        yPar = self.find(y)

        if xPar == yPar:
            return
        
        if self.rank[xPar] < self.rank[yPar]:
            self.parent[xPar] = yPar
        elif self.rank[xPar] > self.rank[yPar]:
            self.parent[yPar] = xPar
        else:
            self.parent[xPar] = yPar
            self.rank[xPar]  += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        # Step 1: Union all connected indices
        for src, dest in pairs: # E. alpha(V)
            uf.union(src, dest) # E Edges
        
        # Group indices by their group representative
        root_to_indices = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            root_to_indices[root].append(i)
        
        # Step 3: For each connected component, sort its characters and assign
        res = list(s)
        for indices in root_to_indices.values():
            chars = [s[i] for i in indices]
            indices.sort()
            chars.sort()

            for idx, ch in zip(indices, chars):
                res[idx] = ch
        
        return "".join(res)
    
        