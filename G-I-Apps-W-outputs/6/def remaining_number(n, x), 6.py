
def remaining_number(n, x):
    ans = x * 2
    print(ans)

T = int(input())
for _ in range(T):
    n, x = map(int, input().split())
    remaining_number(n, x)
