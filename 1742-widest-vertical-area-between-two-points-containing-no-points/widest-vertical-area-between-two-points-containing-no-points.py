class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        x = []
        for i in points:
            x.append(i[0])

        x = [x[j-1]-x[j] for j in range(1,len(x))]
        return abs(min(x))

        