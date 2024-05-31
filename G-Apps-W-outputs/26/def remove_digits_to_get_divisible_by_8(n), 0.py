
def remove_digits_to_get_divisible_by_8(n):
    n = str(n)
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            for k in range(j + 1, len(n)):
                num = int(n[i] + n[j] + n[k])
                if num % 8 == 0:
                    return "YES\n" + str(num)
    return "NO"

# Input
n = int(input().strip())

# Output
print(remove_digits_to_get_divisible_by_8(n))
