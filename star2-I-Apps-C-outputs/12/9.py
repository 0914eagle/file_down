
def solve(n, d):
    pass

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n - 1)]
    print(solve(n, d))

if __name__ == '__main__':
    main()

