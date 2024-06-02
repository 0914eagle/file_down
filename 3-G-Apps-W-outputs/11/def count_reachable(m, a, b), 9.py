
def count_reachable(m, a, b):
    if a == 1 or b == 1:
        return m + 1
    
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    lcm_ab = lcm(a, b)
    period = lcm_ab - a - b
    
    def f(x):
        if x < 0:
            return 0
        return x // lcm_ab * period + min(period, x % lcm_ab + 1)
    
    return sum(f(i) for i in range(m + 1))

# Input
m, a, b = map(int, input().split())

# Output
print(count_reachable(m, a, b))
