
N, L = map(int, input().split())
apples = [L] + list(range(L+1, L+N))
sums = [sum(apples[:i]+apples[i+1:]) for i in range(N)]
diff = [abs(sums[i]-sums[0]) for i in range(1, N)]
print(sums[diff.index(min(diff))+1])

