
def proportion_watered(a, b, c, d):
    a = a % 90
    b = b % 90
    c = c % 90
    d = d % 90
    
    if a + c >= 90 or b + d >= 90:
        return 1.0
    
    if a + b + c + d == 0:
        return 0.0
    
    if a + c <= b + d:
        return 0.5 * (1 - (a + c) / 90)
    else:
        return 0.5 * (1 - (b + d) / 90)

# Sample Input
a, b, c, d = 45, 45, 0, 0
print(proportion_watered(a, b, c, d))
