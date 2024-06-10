
def solve(n, schedule):
    pass

if __name__ == "__main__":
    n = int(input())
    schedule = [list(map(int, input().split())) for _ in range(n-1)]
    print(solve(n, schedule))

