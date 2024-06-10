
n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

a.sort()

for i in range(m):
    total = sum(a[:q[i] - 1])
    total += sum(a[q[i]:])
    print(total)

