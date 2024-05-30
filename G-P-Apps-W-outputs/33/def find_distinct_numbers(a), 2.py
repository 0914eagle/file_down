
def find_distinct_numbers(a):
    count = 1
    for i in range(len(a) - 1):
        if int(a[i]) + int(a[i + 1]) == 9:
            count += 1
    if a[0] == '9' or a[-1] == '9':
        count = (count + 1) // 2
    return min(count, (len(a) + 1) // 2)

# Read input
a = input().strip()

# Output
print(find_distinct_numbers(a))
```
