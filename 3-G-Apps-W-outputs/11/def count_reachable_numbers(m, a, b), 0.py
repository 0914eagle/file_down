
def count_reachable_numbers(m, a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def f(x):
        if x < a:
            return x + 1
        if a > b:
            return x + 1
        return x // gcd(a, b) + 1

    total_sum = 0
    for i in range(m + 1):
        total_sum += f(i)

    return total_sum

# Input
m, a, b = map(int, input().split())

# Output
print(count_reachable_numbers(m, a, b))
