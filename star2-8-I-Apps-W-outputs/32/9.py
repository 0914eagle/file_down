
t = int(input())
for _ in range(t):
    a, b, n, m = map(int, input().split())
    if a == 0 or b == 0:
        print("No")
    elif a >= n + m and b >= n + m:
        print("Yes")
    elif a < n + m and b < n + m:
        print("No")
    else:
        if a > b:
            print("Yes")
        else:
            print("No")

