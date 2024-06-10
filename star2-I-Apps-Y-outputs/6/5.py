
import sys

def solve(n, x, y):
    x.sort()
    y.sort()
    path = ''
    for i in range(n):
        path += 'R' * x[i]
        path += 'U' * y[i]
    return path

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        x = [0] * n
        y = [0] * n
        for i in range(n):
            x[i], y[i] = map(int, sys.stdin.readline().strip().split())
        path = solve(n, x, y)
        print('YES')
        print(path)

if __name__ == '__main__':
    main()

