
n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        if a[i] + a[j] in a[j+1:]:
            count += 1
print(count)

