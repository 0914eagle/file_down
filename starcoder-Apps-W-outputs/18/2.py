
n = int(input())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))
x = 1
while x < n:
    for i in range(1, 5):
        if a[x-1][i-1] != 0:
            if a[x-1][i-1] == b[x][i-1]:
                x += 1
                break
            else:
                print("No")
                exit(0)
        else:
            break
    if i == 4:
        print("No")
        exit(0)
print("Yes")
