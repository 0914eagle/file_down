
n = int(input())
max_div = 0
max_num = 0
for i in range(1, n + 1):
    div = 0
    num = i
    while num % 2 == 0:
        div += 1
        num //= 2
    if div > max_div:
        max_div = div
        max_num = i
print(max_num)

