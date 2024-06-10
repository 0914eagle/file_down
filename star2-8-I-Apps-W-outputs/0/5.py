
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 0
for x in a:
    lb = 0
    rb = m - 1
    while lb <= rb:
        mid = (lb + rb) // 2
        if x + b[mid] == 1:
            ans += 1
            break
        elif x + b[mid] < 1:
            lb = mid + 1
        else:
            rb = mid - 1
print(ans)

