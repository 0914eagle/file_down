
x = int(input())
result = 0

if x >= 500:
    result += x // 500 * 1000
    x %= 500

result += x // 5 * 5

print(result)

