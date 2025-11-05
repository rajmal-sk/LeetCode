class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        free_rooms = []
        intervals.sort(key= lambda x : x[0])

        # Here in the heap we are using the meeting end time only
        heapq.heappush(free_rooms, (intervals[0][1], intervals[0][0]))

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if free_rooms[0][0] <= start:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, (end, start))
        
        return len(free_rooms)