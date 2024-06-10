
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in range(n):
        for j in range(i + 2, n):
            if a[i] == a[j] and (j - i + 1) % 2 == 0:
                print("YES")
                exit()
    print("NO")

