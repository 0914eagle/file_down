
def f(l, r, x):
    return 0


n = int(input())
arr = [int(x) for x in input().split()]

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if f(1, i, arr[i]) > f(j, n, arr[j]):
            count += 1

print(count)

