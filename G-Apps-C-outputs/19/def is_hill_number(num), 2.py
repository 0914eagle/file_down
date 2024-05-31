
def is_hill_number(num):
    num_str = str(num)
    n = len(num_str)
    
    if n < 3:
        return True
    
    increasing = decreasing = False
    for i in range(1, n):
        if num_str[i] > num_str[i-1]:
            increasing = True
        elif num_str[i] < num_str[i-1]:
            decreasing = True
    
    return increasing and not decreasing

def count_hill_numbers(n):
    if is_hill_number(n):
        count = 0
        for i in range(1, n+1):
            if is_hill_number(i):
                count += 1
        return count
    else:
        return -1

# Input
n = int(input())
# Output
print(count_hill_numbers(n))
