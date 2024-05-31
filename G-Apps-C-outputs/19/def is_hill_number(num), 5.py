
def is_hill_number(num):
    num_str = str(num)
    increasing = True
    decreasing = False

    for i in range(1, len(num_str)):
        if num_str[i] < num_str[i - 1]:
            increasing = False
        if num_str[i] > num_str[i - 1]:
            decreasing = True

    return increasing and decreasing

def count_hill_numbers(n):
    if not is_hill_number(n):
        return -1

    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1

    return count

# Input processing and output
n = int(input())
result = count_hill_numbers(n)
print(result)
