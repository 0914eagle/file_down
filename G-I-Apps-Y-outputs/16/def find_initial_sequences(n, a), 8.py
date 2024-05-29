
def find_initial_sequences(n, a):
    increasing = []
    decreasing = []
    
    prev = a[0]
    increasing.append(a[0])
    
    for i in range(1, n):
        if a[i] > prev:
            increasing.append(a[i])
        elif a[i] < prev:
            decreasing.insert(0, a[i])
        else:
            return "NO"
        prev = a[i]
    
    seq_len = len(increasing) + len(decreasing)
    if seq_len != n:
        return "NO"
    
    return "YES\n{}\n{}\n{}\n{}".format(len(increasing), ' '.join(map(str, increasing)), len(decreasing), ' '.join(map(str, decreasing))

# Input parsing
n = int(input())
a = list(map(int, input().split()))

# Call the function and print the result
result = find_initial_sequences(n, a)
print(result)
```
