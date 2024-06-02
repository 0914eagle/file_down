
def solve(N):
    max_div = 0
    ans = 0
    for i in range(1, N+1):
        div = 0
        while i % 2 == 0:
            i //= 2
            div += 1
        if div > max_div:
            max_div = div
            ans = i
    return ans

N = int(input())
print(solve(N))

