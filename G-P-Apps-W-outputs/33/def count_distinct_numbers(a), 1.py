
def count_distinct_numbers(a):
    a = list(map(int, str(a)))
    nines_count = a.count(9)
    result = 1
    for i in range(len(a)-1):
        if a[i] + a[i+1] == 9:
            result += 1
            a[i] = 9
            a[i+1] = 0
    if a[-1] == 9:
        nines_count += 1
    return min(nines_count, result)

# Read input
a = int(input().strip())

# Call the function and print the result
print(count_distinct_numbers(a))
```
