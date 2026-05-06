class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        topSort = []

        for a, b in prerequisites:
            indegrees[a] += 1
            graph[b].append(a)
        
        queue = []

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.pop(0)
            topSort.append(node)

            for neighbour in graph[node]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    queue.append(neighbour)
        
        return topSort if len(topSort) == numCourses else []