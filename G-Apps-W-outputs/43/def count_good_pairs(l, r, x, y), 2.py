
def count_good_pairs(l, r, x, y):
    gcd = y // x
    count = 0
    for a in range(max(l, x), min(r, y) + 1):
        b = a * gcd
        if l <= a <= r and l <= b <= r and a * b // gcd == y:
            count += 1
    return count

# Input
l, r, x, y = map(int, input().split())

# Output
print(count_good_pairs(l, r, x, y))
