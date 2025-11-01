class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        print(points)
        left = 0
        count = 1
        for i in range(1, len(points)):
            if points[i][0] > points[left][1]:
                left = i
                count += 1
        return count