
def count_nums(arr):
    total_count = 0
    for num in arr:
        if num < 0:
            digits = [int(d) for d in str(num)[1:]]
        else:
            digits = [int(d) for d in str(num)]
        
        if sum(digits) > 0:
            total_count += 1
    
    return total_count

# Test cases
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)
