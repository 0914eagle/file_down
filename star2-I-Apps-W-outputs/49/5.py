
def solve(n, m, map):
    return 0, [[]]

if __name__ == "__main__":
    n, m = map(int, input().split())
    map = []
    for i in range(n):
        map.append(input())
    T, map = solve(n, m, map)
    print(T)
    for line in map:
        print("".join(line))

