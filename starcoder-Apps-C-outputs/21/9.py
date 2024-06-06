
n = list(map(int, input().split()))
if n[0] < n[3] or n[0] < n[2] or n[2] < n[1]:
    print("NO")
else:
    print("YES")
    for i in range(n[0] - n[1]):
        print(0, end = ' ')
    for i in range(n[1]):
        print(1, end = ' ')
    for i in range(n[2] - n[3]):
        print(2, end = ' ')
    for i in range(n[3]):
        print(3, end = ' ')
