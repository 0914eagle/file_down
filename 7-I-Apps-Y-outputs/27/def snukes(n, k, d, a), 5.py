
import sys

def snukes(n, k, d, a):
    count = 0
    for i in range(k):
        for j in range(d[i]):
            if a[i][j] == 1:
                count += 1
    return count

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    d = [int(x) for x in sys.stdin.readline().split()]
    a = []
    for i in range(k):
        a.append([int(x) for x in sys.stdin.readline().split()])
    print(snukes(n, k, d, a))

