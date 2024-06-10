
from typing import List, Tuple


class Solution:
    def minimumVerticalMoves(self, malls: List[Tuple[int, int, int]]) -> int:
        n = len(malls)
        m = len(set(t for x, y, t in malls))
        locations = [[] for _ in range(m)]
        for i, (x, y, t) in enumerate(malls):
            locations[t - 1].append((x, y, i))
        min_moves = [float("inf")] * n

        for i in range(m):
            x, y, idx = locations[i][0]
            min_moves[idx] = 0

            for x, y, idx in locations[i][1:]:
                min_moves[idx] = 0

        for i in range(m):
            for j in range(i + 1, m):
                x1, y1, idx1 = locations[i][0]
                x2, y2, idx2 = locations[j][0]
                min_moves[idx1] = min(
                    min_moves[idx1], abs(x2 - x1) + abs(y2 - y1)
                )
                min_moves[idx2] = min(
                    min_moves[idx2], abs(x2 - x1) + abs(y2 - y1)
                )

                for x1, y1, idx1 in locations[i][1:]:
                    for x2, y2, idx2 in locations[j][1:]:
                        min_moves[idx1] = min(
                            min_moves[idx1], abs(x2 - x1) + abs(y2 - y1)
                        )
                        min_moves[idx2] = min(
                            min_moves[idx2], abs(x2 - x1) + abs(y2 - y1)
                        )

        return sum(min_moves)


if __name__ == "__main__":
    s = Solution()
    print(s.minimumVerticalMoves([(1, 1, 2), (1, 2, 1), (-1, 1, 2)]))


