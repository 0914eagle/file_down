
def is_hill_number(n):
    n_str = str(n)
    increasing = True
    decreasing = True
    for i in range(1, len(n_str)):
        if n_str[i] < n_str[i-1]:
            increasing = False
        if n_str[i] > n_str[i-1]:
            decreasing = False
    return increasing or decreasing

def count_hill_numbers(n):
    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1
    return count if is_hill_number(n) else -1

# Input
n = int(input())

# Output
print(count_hill_numbers(n))
