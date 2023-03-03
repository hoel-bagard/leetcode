import math

from typing_extensions import Self


class Solution:
    def nearestValidPoint(self: Self, x: int, y: int, points: list[list[int]]) -> int:  # noqa: N802
        min_dist, min_idx = math.inf, -1
        for i, (point_x, point_y) in enumerate(points):
            if (x == point_x or y == point_y) and (dist := abs(x - point_x) + abs(y - point_y)) < min_dist:
                min_dist, min_idx = dist, i
        return min_idx


# class Solution:
#     def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
#         return min(map(lambda idx_point: (idx_point[0], abs(x - idx_point[1][0]) + abs(y - idx_point[1][1])),
#                        ((idx, point) for (idx, point) in enumerate(points) if x == point[0] or y == point[1])),
#                    default=(-1, None),
#                    key=lambda idx_point: idx_point[1])[0]


# Worst solution.
# class Solution:
#     def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
#         (dists := list(map(lambda idx_point: (idx_point[0], abs(x - idx_point[1][0]) + abs(y - idx_point[1][1])),
#                            enumerate(points)))).sort(key=lambda idx_point: idx_point[1])
#         for idx, _dist in dists:
#             if points[idx][0] == x or points[idx][1] == y:
#                 return idx
#         return -1
