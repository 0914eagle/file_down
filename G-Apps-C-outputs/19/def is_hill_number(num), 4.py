
def is_hill_number(num):
    num_str = str(num)
    n = len(num_str)
    
    if n == 1:
        return True
    
    increasing = True
    
    for i in range(1, n):
        if num_str[i] == num_str[i-1]:
            continue
        if num_str[i] > num_str[i-1]:
            increasing = True
        else:
            if increasing:
                increasing = False
            else:
                return False
    
    return True

def count_hill_numbers(n):
    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1
    return count

n = int(input())
if is_hill_number(n):
    print(count_hill_numbers(n))
else:
    print(-1)
