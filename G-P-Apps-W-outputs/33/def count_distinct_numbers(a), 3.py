
def count_distinct_numbers(a):
    a = list(map(int, str(a)))
    nines = []
    distinct_numbers = set()
    
    for i in range(len(a) - 1):
        if a[i] + a[i+1] == 9:
            nines.append(1)
        else:
            nines.append(0)
    
    nines.append(0)  # Dummy zero at the end to make indexing consistent
    
    start = 0
    end = 0
    while end < len(nines):
        if nines[end] == 0:
            if start < end:
                distinct_numbers.add(tuple(a[:start] + [9] + a[end+1:]))
            start = end + 1
        end += 1
    
    return len(distinct_numbers)

# Read input
a = int(input().strip())

# Calculate and print the number of distinct numbers
print(count_distinct_numbers(a))
```
