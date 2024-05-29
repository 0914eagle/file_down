
def get_operations(a, b):
    def divisors(n):
        divs = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                divs.append(d)
                while n % d == 0:
                    n //= d
            d += 1
        if n > 1:
            divs.append(n)
        return divs

    a_divs = divisors(a)
    b_divs = divisors(b)

    if a == b:
        return 0

    if set(a_divs) != set(b_divs):
        return -1

    max_div = max(set(a_divs + b_divs))

    a_ops = 0
    while a % max_div == 0:
        a //= max_div
        a_ops += 1

    b_ops = 0
    while b % max_div == 0:
        b //= max_div
        b_ops += 1

    return abs(a_ops - b_ops)

a, b = map(int, input().split())
result = get_operations(a, b)
print(result)
```
