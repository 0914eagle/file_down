
def proportion_watered(a, b, c, d):
    a = a % 90
    b = b % 90
    c = c % 90
    d = d % 90

    if a + c >= 90 or b + d >= 90:
        return 1.0

    if a + b <= 90 and c + d <= 90:
        return 0.0

    if a + b > 90 and c + d > 90:
        return 0.5

    if a + b > 90:
        return (90 - a) / 90

    if c + d > 90:
        return (90 - c) / 90

a, b, c, d = map(float, input().split())
result = proportion_watered(a, b, c, d)
print(result)
