

from typing import List
class Solution:
    def dfs(self, current: int, res: List[int], used: List[bool]) -> int:
        if used[current]:
            return 0
        used[current] = True
        ans = res[current]
        for i in range(len(res[current])):
            if res[current][i] == 0:
                ans = min(ans, self.dfs(i, res, used))
        return ans
    def solve(self, res: List[List[int]], n: int) -> int:
        used = [False] * n
        ans = 0
        for i in range(n):
            ans += self.dfs(i, res, used)
        return ans

    def main(self) -> None:
        n = int(input())
        res = [[] for _ in range(n)]
        for _ in range(n):
            p = int(input())
            for _ in range(p):
                l, k, *d = list(map(int, input().split()))
                res[d[0]].append(l)
        print(self.solve(res, n))
Solution().main()
