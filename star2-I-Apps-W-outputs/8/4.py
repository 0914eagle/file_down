
def solve(n, m, a, queries):
    for l, r, x in queries:
        for i in range(l, r+1):
            if a[i-1] != x:
                print(i)
                break
        else:
            print(-1)


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(m)]
    solve(n, m, a, queries)


if __name__ == "__main__":
    main()

