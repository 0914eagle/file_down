
def frog_jump_sum(m, a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def f(x):
        if x < b:
            return x + 1
        g = gcd(a, b)
        if x < g:
            return x + 1
        return f(x - g) + 1

    total_sum = 0
    for i in range(m + 1):
        total_sum += f(i)

    return total_sum

# Input
m, a, b = map(int, input().split())

# Output
print(frog_jump_sum(m, a, b))
