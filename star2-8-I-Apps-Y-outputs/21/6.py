
x = int(input())
count_500 = x // 500
x %= 500
count_5 = x // 5
print(count_500 * 1000 + count_5 * 5)

