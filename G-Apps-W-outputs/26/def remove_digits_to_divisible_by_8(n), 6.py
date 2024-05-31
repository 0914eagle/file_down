
def remove_digits_to_divisible_by_8(n):
    if len(n) <= 2:
        if int(n) % 8 == 0:
            return "YES", n
        else:
            return "NO", ""

    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            for k in range(j + 1, len(n)):
                num = int(n[i] + n[j] + n[k])
                if num % 8 == 0:
                    return "YES", str(num)

    return "NO", ""

# Input
n = input().strip()

# Output
result, new_num = remove_digits_to_divisible_by_8(n)
print(result)
if result == "YES":
    print(new_num)
