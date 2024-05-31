
def is_hill_number(n):
    n_str = str(n)
    i = 1
    
    # Check if digits rise at the beginning
    while i < len(n_str) and n_str[i] >= n_str[i-1]:
        i += 1
    
    # Check if digits fall at the end
    while i < len(n_str) and n_str[i] <= n_str[i-1]:
        i += 1
    
    if i == len(n_str):
        return True
    else:
        return False

def count_hill_numbers(n):
    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1
    return count

def solve_hill_number_problem(n):
    if is_hill_number(n):
        return count_hill_numbers(n)
    else:
        return -1

# Input
n = int(input())

# Output
print(solve_hill_number_problem(n))
