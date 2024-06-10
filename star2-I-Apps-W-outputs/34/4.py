
def solve(n, k, a):
    return [(k % 2) * d for d in a]

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(*solve(n, k, a))

if __name__ == '__main__':
    main()

