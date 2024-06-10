
n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

a.sort()

for i in q:
    print(sum(a[:i-1]) + sum(a[i:]))

