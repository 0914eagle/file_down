
def solve(n, m, groups):
    return "YES" if n == 1 else "NO"

def main():
    n, m = map(int, input().split())
    groups = []
    for _ in range(m):
        k, *v = map(int, input().split())
        groups.append(v)
    print(solve(n, m, groups))

if __name__ == "__main__":
    main()

