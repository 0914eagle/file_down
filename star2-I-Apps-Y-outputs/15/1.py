
import math

def count_odd_numbers_with_exactly_eight_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            num_divisors = 0
            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    num_divisors += 2
            if num_divisors == 8:
                count += 1
    return count

n = int(input())
print(count_odd_numbers_with_exactly_eight_divisors(n))

