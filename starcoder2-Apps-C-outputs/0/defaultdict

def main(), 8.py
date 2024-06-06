
from collections import defaultdict

def main():
    n = int(input())
    d = defaultdict(int)
    for _ in range(n):
        k = int(input())
        for _ in range(k):
            a, b = map(int, input().split())
            d[b] += a
    for i in sorted(d):
        print(d[i], end=' ')

if __name__ == '__main__':
    main()
