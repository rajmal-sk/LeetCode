class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        order = []
        graph = defaultdict(list)

        for u , v in prerequisites:
            indegrees[u] += 1
            graph[v].append(u)
        
        queue = []

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.pop(0)
            order.append(node)

            for neighbour in graph[node]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    queue.append(neighbour)
        

        return len(order) == numCourses