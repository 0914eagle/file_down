
def is_hill_number(n):
    num_str = str(n)
    is_hill = True
    increasing = True
    decreasing = False
    
    if len(num_str) < 3:
        return False
    
    for i in range(1, len(num_str)):
        if num_str[i] > num_str[i-1]:
            if decreasing:
                is_hill = False
                break
            increasing = True
            decreasing = False
        elif num_str[i] < num_str[i-1]:
            if not increasing:
                is_hill = False
                break
            increasing = False
            decreasing = True
        else:
            is_hill = False
            break
    
    return is_hill

def count_hill_numbers(n):
    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1
    
    return count if is_hill_number(n) else -1

# Read input
n = int(input())

# Output result
print(count_hill_numbers(n))
