
def solve(n, k):
    # your code goes here

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

