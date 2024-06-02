
def max_divisible_by_3(s):
    count = 0
    for i in range(1, len(s)):
        if (int(s[i-1]) + int(s[i])) % 3 == 0:
            count += 1
    return count

# Read input
s = input().strip()

# Call the function and print the result
print(max_divisible_by_3(s))