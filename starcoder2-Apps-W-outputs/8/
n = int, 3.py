
n = int(input())
a = list(map(int, input().split()))

l, r = 0, 0

for i in range(n):
    for j in range(i, n):
        if a[i:j+1].count(max(a[i:j+1])) == len(a[i:j+1]):
            l, r = i, j

print(l+1, r+1)
