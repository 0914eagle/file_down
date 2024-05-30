
import sys

def get_input():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    return n, m, c, b, a

def solve(n, m, c, b, a):
    count = 0
    for i in range(n):
        total = 0
        for j in range(m):
            total += a[i][j] * b[j]
        if total + c > 0:
            count += 1
    return count

if __name__ == "__main__":
    n, m, c, b, a = get_input()
    print(solve(n, m, c, b, a))

