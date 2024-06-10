
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 2):
        if a[i] == a[n - 1] and a[i + 1] == a[n - 2]:
            print("YES")
            break
    else:
        print("NO")

