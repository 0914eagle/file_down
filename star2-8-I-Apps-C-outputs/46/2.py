
def chinese_remainder(n, a):
    
    sum = 0
    prod = 1
    for i in range(len(n)):
        prod *= n[i]
    for i in range(len(n)):
        p = prod // n[i]
        sum += a[i] * mul_inv(p, n[i]) * p
    return sum % prod


def mul_inv(a, b):
    
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main():
    
    m = list(map(int, input().split()))
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    n = [mi - yi for mi, yi in zip(m, y)]
    a = [xi - yi for xi, yi in zip(x, y)]
    print(chinese_remainder(n, a))


if __name__ == '__main__':
    main()

