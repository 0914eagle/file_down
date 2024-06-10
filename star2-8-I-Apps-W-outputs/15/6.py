
n = int(input())
a = [int(x) for x in input().split()]
if sum(a[:n]) == sum(a[n:]):
    print(-1)
else:
    print(' '.join([str(x) for x in a]))

