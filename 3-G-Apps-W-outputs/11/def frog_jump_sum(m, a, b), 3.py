
def frog_jump_sum(m, a, b):
    if a == 1 and b == 1:
        return m + 1

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    lcm = (a * b) // gcd(a, b)
    period = lcm - a - b

    def f(x):
        if x < a:
            return x + 1
        if x < b:
            return f(a - 1) + 1
        if x < lcm:
            return f(b - 1) + 1
        return f(x % period)

    return sum(f(i) for i in range(m + 1))

# Input parsing
m, a, b = map(int, input().split())
print(frog_jump_sum(m, a, b))
