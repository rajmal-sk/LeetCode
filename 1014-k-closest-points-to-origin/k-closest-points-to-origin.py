class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict = SortedDict()

        for x1, y1 in points:
            dist = x1 ** 2 + y1 ** 2
            if dist not in dict:
                dict[dist] = []
            dict[dist].append([x1, y1])
        
        res = []
        remain = k
        for points in dict.values():
            n = len(points)
            if remain - n >= 0:
                res.extend(points[:])
            else:
                break
            remain = remain - n
        return res