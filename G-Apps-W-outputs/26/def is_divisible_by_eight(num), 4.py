
def is_divisible_by_eight(num):
    return int(num) % 8 == 0

def remove_digits_to_divisible_by_eight(n):
    n_str = str(n)
    n_len = len(n_str)

    for i in range(n_len):
        for j in range(i+1, n_len):
            for k in range(j+1, n_len):
                new_num = n_str[:i] + n_str[j] + n_str[k]
                if is_divisible_by_eight(new_num):
                    return "YES\n" + new_num

    return "NO"

# Input
n = input().strip()

# Solve
result = remove_digits_to_divisible_by_eight(n)

# Output
print(result)
