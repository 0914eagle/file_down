
def solve(N, a):
    balls = set()
    for i in range(1, N+1):
        if a[i-1] == 1:
            balls.add(i)
    print(len(balls))
    print(*balls)

N = int(input())
a = list(map(int, input().split()))
solve(N, a)

