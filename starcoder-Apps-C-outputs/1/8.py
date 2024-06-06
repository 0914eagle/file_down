

def get_digit(n):
    prod = 1
    while n > 0:
        if n % 10 != 0:
            prod = prod * (n % 10)
        n = n // 10
    return prod

l, r = map(int, input().split())

res = [0] * 9

for i in range(l, r + 1):
    res[get_digit(i) - 1] += 1

print(*res)
