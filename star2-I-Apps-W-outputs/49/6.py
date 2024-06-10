
def solve(n, m, map):
    pass

def main():
    n, m = map(int, input().split())
    map = [input() for _ in range(n)]
    T, map = solve(n, m, map)
    print(T)
    for row in map:
        print(row)

if __name__ == "__main__":
    main()

