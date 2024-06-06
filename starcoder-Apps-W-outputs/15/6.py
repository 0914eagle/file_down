
#O(n^2) implementation
from collections import defaultdict
class Solution:
    def __init__(self, arr):
        self.mp = defaultdict(lambda:set())
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if self.check(arr[i], arr[j]):
                    self.mp[i].add(j)
                    self.mp[j].add(i)

    def check(self, a, b):
        return a[0] < b[0] < a[1] or a[0] < b[1] < a[1]

    def solve(self, a, b):
        n = len(self.mp)
        visited = [False]*n
        queue = [a]
        while queue:
            top = queue.pop(0)
            visited[top] = True
            for ele in self.mp[top]:
                if ele == b:
                    return True
                if not visited[ele]:
                    queue.append(ele)
        return False

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    ob = Solution(arr)
    q = int(input())
    while q:
        a, b = map(int, input().split())
        print("YES" if ob.solve(a-1, b-1) else "NO")
        q -= 1

main()
