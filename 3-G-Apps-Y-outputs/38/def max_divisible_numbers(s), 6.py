
def max_divisible_numbers(s):
    count = 0
    for i in range(len(s)):
        if int(s[i]) % 3 == 0:
            count += 1
        elif i > 0 and (int(s[i-1]) + int(s[i])) % 3 == 0:
            count += 1
    return count

# Input
s = input().strip()

# Output
print(max_divisible_numbers(s))
