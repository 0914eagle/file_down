
def count_distinct_numbers(a):
    a = list(str(a))
    nines = 0
    for i in range(len(a)-1):
        if int(a[i]) + int(a[i+1]) == 9:
            a[i] = '9'
            a[i+1] = ''
            nines += 1
    return nines + 1

# Input
a = int(input().strip())

# Output
print(count_distinct_numbers(a))
```
