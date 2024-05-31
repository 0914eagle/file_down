
import math

def count_good_pairs(l, r, x, y):
    gcd = math.gcd(x, y)
    lcm = x * y // gcd
    
    count = 0
    for a in range(l, r+1):
        if x <= a <= y and lcm % a == 0 and math.gcd(lcm // a, a) == x:
            count += 1
    
    return count

# Input processing
l, r, x, y = map(int, input().split())

# Call the function and print the result
print(count_good_pairs(l, r, x, y))
