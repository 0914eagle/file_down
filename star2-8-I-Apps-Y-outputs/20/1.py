
n = int(input())

max_div = 0
ans = 1
for i in range(1, n + 1):
    div = 0
    temp = i
    while temp % 2 == 0:
        div += 1
        temp //= 2
    
    if div > max_div:
        max_div = div
        ans = i
    
print(ans)

