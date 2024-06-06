
# https://atcoder.jp/contests/abc176/tasks/abc176_c
n = int(input())
a = list(map(int, input().split()))

r = 0
t = a[0]
for i in range(1, n):
    if a[i] < t:
        r += t - a[i]
    else:
        t = a[i]

print(r)
