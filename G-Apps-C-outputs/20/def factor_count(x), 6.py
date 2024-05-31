
from math import gcd

MOD = 10**9 + 7

def factor_count(x):
    count = 0
    i = 1
    while i*i <= x:
        if x % i == 0:
            if i*i == x:
                count += 1
            else:
                count += 2
        i += 1
    return count

def count_ways(n, students):
    factors = [factor_count(x) for x in students]
    total_ways = 1

    for i in range(n):
        common_factors = 0
        for j in range(n):
            if i != j and gcd(students[i], students[j]) > 1:
                common_factors += 1
        total_ways = (total_ways * (2**common_factors - 1)) % MOD

    return total_ways

# Read input
n = int(input())
students = [int(input()) for _ in range(n)]

# Calculate the number of ways and output the result
print(count_ways(n, students))
