
def solve(N):
    ans = 0
    for i in range(1, N+1):
        cnt = 0
        while i % 2 == 0:
            i //= 2
            cnt += 1
        if cnt > ans:
            ans = cnt
    return ans

N = int(input())
print(solve(N))

