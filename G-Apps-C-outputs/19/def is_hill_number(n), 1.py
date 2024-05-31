
def is_hill_number(n):
    num_str = str(n)
    if len(num_str) < 3:
        return True
    increasing = False
    decreasing = False
    for i in range(1, len(num_str)):
        if num_str[i] > num_str[i-1]:
            increasing = True
        elif num_str[i] < num_str[i-1]:
            decreasing = True
        if increasing and decreasing:
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
