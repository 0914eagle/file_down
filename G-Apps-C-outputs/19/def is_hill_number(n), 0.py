
def is_hill_number(n):
    num_str = str(n)
    n_digits = len(num_str)
    
    if n_digits == 1:
        return True
    
    increasing = True
    decreasing = True
    for i in range(1, n_digits):
        if num_str[i] > num_str[i-1]:
            decreasing = False
        if num_str[i] < num_str[i-1]:
            increasing = False
    
    return not (increasing and decreasing)

def count_hill_numbers(n):
    if not is_hill_number(n):
        return -1
    
    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1
    
    return count

n = int(input())
result = count_hill_numbers(n)
print(result)
