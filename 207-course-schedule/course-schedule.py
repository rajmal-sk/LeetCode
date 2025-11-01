class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for edge in prerequisites:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            indegree[v] += 1
        
        queue  = deque()
        topSort = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()

            topSort.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return len(topSort) == numCourses