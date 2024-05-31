
def find_number(m, n, p, q):
    for i in range(10**(m-1), 10**m):
        num_str = str(i)
        if len(num_str) >= n + len(str(p)):
            first_part = num_str[:n]
            second_part = num_str[n:]
            new_num_str = int(second_part + str(p))
            if new_num_str * q == i:
                return i
    return "IMPOSSIBLE"

# Input processing
m, n, p, q = map(int, input().split())

# Call the function and print the result
result = find_number(m, n, p, q)
print(result)
