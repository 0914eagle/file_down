
def solve(n, m, k, maze):
    return "IMPOSSIBLE"


def main():
    n, m, k = map(int, input().split())
    maze = [input() for _ in range(n)]
    
    print(solve(n, m, k, maze))


if __name__ == '__main__':
    main()

