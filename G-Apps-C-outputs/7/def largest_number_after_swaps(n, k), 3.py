
def largest_number_after_swaps(n, k):
    digits = list(str(n))
    for i in range(len(digits)):
        if k == 0:
            break
        max_digit = max(digits[i:])
        if digits[i] != max_digit:
            max_index = len(digits) - digits[::-1].index(max_digit) - 1
            if i != max_index:
                digits[i], digits[max_index] = digits[max_index], digits[i]
                k -= 1
    return int("".join(digits))

# Read input values
n, k = map(int, input().split())

# Find the largest number after k swaps
result = largest_number_after_swaps(n, k)
print(result)
