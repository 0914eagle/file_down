
def max_divisible_by_3(s):
    count = 0
    remainder_count = [0, 0, 0]
    
    for digit in s:
        remainder = int(digit) % 3
        remainder_count[remainder] += 1
    
    total_remainder = sum(remainder_count)
    
    if total_remainder == 1:
        return 0
    elif total_remainder == 2:
        if remainder_count[0] > 0:
            return 1
        elif remainder_count[1] >= 2 or remainder_count[2] >= 2:
            return 1
        else:
            return 0
    else:
        return remainder_count[0] + min(remainder_count[1], remainder_count[2]) + (abs(remainder_count[1] - remainder_count[2]) // 3)

# Input
s = input().strip()

# Output
print(max_divisible_by_3(s))
