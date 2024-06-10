
n = int(input())
a = list(map(int, input().split()))

unique = {}
for i in range(n-1, -1, -1):
    if a[i] not in unique:
        unique[a[i]] = i

print(len(unique))
print(*[k for k in unique.keys()])

