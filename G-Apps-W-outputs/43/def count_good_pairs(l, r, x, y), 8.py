
def count_good_pairs(l, r, x, y):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    count = 0
    for a in range(l, r + 1):
        if x <= a <= y and y % a == 0 and gcd(a, y // a) == x and lcm(a, y // a) == y:
            count += 1

    return count

# Input reading
l, r, x, y = map(int, input().split())

# Call the function and print the result
print(count_good_pairs(l, r, x, y))
