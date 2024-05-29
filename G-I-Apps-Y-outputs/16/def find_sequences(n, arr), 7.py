
def find_sequences(n, arr):
    increasing = []
    decreasing = []
    last_elem = -1
    for elem in arr:
        if elem > last_elem:
            increasing.append(elem)
            last_elem = elem
        elif elem < last_elem:
            decreasing.append(elem)
            last_elem = elem
        else:
            return "NO"

    if len(increasing) + len(decreasing) != n:
        return "NO"

    return f"YES\n{len(increasing)}\n{' '.join(map(str, increasing))}\n{len(decreasing)}\n{' '.join(map(str, decreasing[::-1]))}"

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(find_sequences(n, arr))
```
