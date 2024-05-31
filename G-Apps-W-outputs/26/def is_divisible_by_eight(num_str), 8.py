
def is_divisible_by_eight(num_str):
    for i in range(1000, 10000):
        if i % 8 == 0:
            if set(str(i)) <= set(num_str):
                return "YES\n" + str(i)
    return "NO"

n = input().strip()

result = is_divisible_by_eight(n)
print(result)
