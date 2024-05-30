
import sys

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        temp = 0
        for j in range(m):
            temp += a[i][j] * b[j]
        if temp + c > 0:
            ans += 1
    print(ans)

main()

