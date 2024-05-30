
def count_distinct_numbers(a):
    count = 0
    a = list(map(int, str(a)))

    while True:
        found = False
        for i in range(len(a) - 1):
            if a[i] + a[i + 1] == 9:
                a[i] = 9
                del a[i + 1]
                found = True
                break

        if not found:
            break

    count += a.count(9)
    return count

# Read input
a = int(input().strip())

# Call the function and output the result
print(count_distinct_numbers(a))
```
