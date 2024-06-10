
def solve(n, m, teleports):
    pass

def main():
    n, m = map(int, input().split())
    teleports = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, teleports))

if __name__ == '__main__':
    main()

