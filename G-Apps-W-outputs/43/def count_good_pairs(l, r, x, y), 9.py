
def count_good_pairs(l, r, x, y):
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    lcm = lambda a, b: a * b // gcd(a, b)
    
    count = 0
    for a in range(l, r+1):
        if y % a == 0 and gcd(a, y // a) == x and lcm(a, y // a) == y:
            count += 1
    
    return count

# Reading input
l, r, x, y = map(int, input().split())

# Output the result
print(count_good_pairs(l, r, x, y))
