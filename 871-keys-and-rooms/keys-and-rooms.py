class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = {0}

        def dfs(node):
            for room in rooms[node]:
                if room not in seen:
                    seen.add(room)
                    dfs(room)
        dfs(0)
        return len(seen) == n