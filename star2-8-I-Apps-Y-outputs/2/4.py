
N = int(input())
a = list(map(int, input().split()))
a.sort()
print(2 * sum(a[1:N//2+1]) - a[0] - a[N//2])

