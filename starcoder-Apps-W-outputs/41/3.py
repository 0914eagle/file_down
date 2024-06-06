
n, m = map(int, input().split())
a = list(map(int, input().split()))
s = set(a)
print(min(n, len(s)))
