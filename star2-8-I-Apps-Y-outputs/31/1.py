
from sys import stdin, stdout

def solve(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+2, n+1):
            if arr[i:j] == arr[i:j][::-1]:
                return "YES"
    return "NO"

def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        arr = list(map(int, stdin.readline().split()))
        stdout.write(solve(arr) + '\n')

if __name__ == '__main__':
    main()

