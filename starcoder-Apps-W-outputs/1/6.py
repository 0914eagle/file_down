
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
    elif n == 2:
        print(a[0]+a[1])
    else:
        print(sum(a))
