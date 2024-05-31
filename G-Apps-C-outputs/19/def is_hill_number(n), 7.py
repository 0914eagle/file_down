
def is_hill_number(n):
    num_str = str(n)
    n_len = len(num_str)
    inc = dec = False
    for i in range(1, n_len):
        if num_str[i] > num_str[i-1]:
            inc = True
        elif num_str[i] < num_str[i-1]:
            dec = True
        if inc and dec:
            return False
    return inc and dec

def count_hill_numbers_less_than_equal_to_n(n):
    if not is_hill_number(n):
        return -1

    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1
    return count

# Input
n = int(input())
# Output
print(count_hill_numbers_less_than_equal_to_n(n))
