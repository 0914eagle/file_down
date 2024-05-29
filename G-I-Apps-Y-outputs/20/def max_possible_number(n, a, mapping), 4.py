
def max_possible_number(n, a, mapping):
    a = list(a)
    for i in range(n):
        if int(a[i]) < mapping[int(a[i]) - 1]:
            break
        a[i] = str(mapping[int(a[i]) - 1])
    return ''.join(a)

# Read input
n = int(input())
a = input().strip()
mapping = list(map(int, input().split()))

# Call the function and print the result
result = max_possible_number(n, a, mapping)
print(result)
```
