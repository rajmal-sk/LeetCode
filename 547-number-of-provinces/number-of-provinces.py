class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        else:
            return self.parent[x]
    
    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        numberOfComponents = n

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] and uf.find(i) != uf.find(j):
                    numberOfComponents -= 1
                    uf.union_set(i, j)
        return numberOfComponents 
    
        