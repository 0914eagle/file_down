
import sys
def solve(s):
    n = len(s)
    dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    dy = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
    x, y = 0, 0
    for c in s:
        x += dx[c]
        y += dy[c]
    if x == y == 0:
        return -1
    left, right = 0, n - 1
    while left < n and right >= 0:
        x, y = 0, 0
        for c in s[left:right + 1]:
            x += dx[c]
            y += dy[c]
        if x == y == 0:
            return left + 1, right + 1
        if x != 0:
            left += 1
            right -= 1
        else:
            right -= 1
    return -1

if __name__ == "__main__":
    input = sys.stdin.readline
    output = sys.stdout.write
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        l, r = solve(s)
        output(f"{l} {r}\n")

