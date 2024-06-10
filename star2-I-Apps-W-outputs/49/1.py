
def solve(n, m, map):
    return 0, [[]]

if __name__ == "__main__":
    n, m = map(int, input().split())
    map = [input() for _ in range(n)]
    T, map = solve(n, m, map)
    print(T)
    for row in map:
        print("".join(row))

