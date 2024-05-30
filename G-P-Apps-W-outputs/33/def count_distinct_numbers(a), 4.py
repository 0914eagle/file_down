
def count_distinct_numbers(a):
    count = 0
    a = list(map(int, str(a)))

    while True:
        changed = False
        for i in range(len(a) - 1):
            if a[i] + a[i + 1] == 9:
                count += 1
                a.pop(i)
                a.pop(i)
                a.insert(i, 9)
                changed = True
                break

        if not changed:
            break

    return count + 1

# Read input
a = int(input())

# Calculate and print the output
print(count_distinct_numbers(a))
```
