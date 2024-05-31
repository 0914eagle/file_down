
def is_hill_number(num):
    num_str = str(num)
    peak_found = False
    valley_found = False
    
    for i in range(1, len(num_str)):
        if int(num_str[i]) < int(num_str[i-1]):
            valley_found = True
        if int(num_str[i]) > int(num_str[i-1]):
            peak_found = True
        if valley_found and peak_found:
            return False
    
    return True

def count_hill_numbers(n):
    if is_hill_number(n):
        count = 0
        for i in range(1, n+1):
            if is_hill_number(i):
                count += 1
        return count
    else:
        return -1

# Read input
n = int(input())

# Output
print(count_hill_numbers(n))
