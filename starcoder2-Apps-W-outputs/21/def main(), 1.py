
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = []
    for _ in range(n):
        a.append(tuple(map(int, sys.stdin.readline().split())))
    a.sort()
    ans = 0
    t = 0
    for x, y in a:
        if x > t:
            ans += 1
            t = x + y
        else:
            t = max(t, x + y)
    print(ans)

if __name__ == "__main__":
    main()
