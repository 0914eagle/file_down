
def calculate_convenience(n, p):
    conveniences = [0] * n
    for i in range(n):
        if i + 1 != p[p[i] - 1]:
            conveniences[i] = 1

    max_convenience = sum(conveniences) * 2

    for i in range(n):
        if conveniences[i] == 1 and conveniences[p[i] - 1] == 1:
            max_convenience += 1

    return max_convenience


# Input processing
n = int(input())
p = list(map(int, input().split()))

# Calculate and output the maximum convenience
print(calculate_convenience(n, p))
```
