
N, L = map(int, input().split())
apples = [L + i for i in range(N)]
remaining = sum(apples) - min(apples)
print(remaining)

