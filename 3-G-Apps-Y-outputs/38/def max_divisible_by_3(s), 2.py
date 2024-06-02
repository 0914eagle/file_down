
def max_divisible_by_3(s):
    count = 0
    remainder_count = [0, 0, 0]  # Count of remainders when divided by 3

    for digit in s:
        remainder = int(digit) % 3
        remainder_count[remainder] += 1

    count += remainder_count[0]  # Numbers that are already divisible by 3

    if remainder_count[1] > 0 and remainder_count[2] > 0:
        count += min(remainder_count[1], remainder_count[2])  # Pairs of remainders 1 and 2 can form numbers divisible by 3
        min_remainder = min(remainder_count[1], remainder_count[2])
        remainder_count[1] -= min_remainder
        remainder_count[2] -= min_remainder

    count += remainder_count[1] // 3 + remainder_count[2] // 3  # Remaining numbers that can be formed by dividing by 3

    return count

# Input
s = input().strip()

# Output
print(max_divisible_by_3(s))
