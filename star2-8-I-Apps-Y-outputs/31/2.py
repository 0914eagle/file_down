
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = "NO"
    for i in range(n - 2):
        if a[i] == a[i + 2]:
            res = "YES"
            break
    print(res)

