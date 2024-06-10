
def solve(n, schedule):
    pass

if __name__ == '__main__':
    n = int(input())
    schedule = []
    for _ in range(n-1):
        schedule.append(list(map(int, input().split())))
    print(solve(n, schedule))

