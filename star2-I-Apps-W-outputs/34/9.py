
def solve(n, k, a):
    return [0] * n

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        res = solve(n, k, a)
        print(*res)

if __name__ == "__main__":
    main()

