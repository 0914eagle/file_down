
def count_distinct_numbers(a):
    a = list(map(int, str(a)))
    nines_count = a.count(9)
    if nines_count == 0:
        return 1
    
    result = 1
    current_nines = 0
    for digit in a:
        if digit == 9:
            current_nines += 1
            if current_nines == nines_count:
                result += 1
                current_nines = 0
        elif digit + a[a.index(digit) + 1] == 9:
            result += 1
    
    return result

# Read input
a = int(input().strip())

# Call the function and print the result
print(count_distinct_numbers(a))
```
