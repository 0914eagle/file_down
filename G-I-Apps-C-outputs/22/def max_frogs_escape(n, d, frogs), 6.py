
def max_frogs_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)
    escape_count = 0
    for i in range(n):
        total_weight = 0
        height_needed = d
        for j in range(i, n):
            if frogs[j][0] >= height_needed:
                escape_count += 1
                break
            if total_weight + frogs[j][1] <= frogs[i][1]:
                total_weight += frogs[j][1]
                height_needed -= frogs[j][2]
                escape_count += 1
    return escape_count

# Input parsing
n, d = map(int, input().split())
frogs = []
for _ in range(n):
    l, w, h = map(int, input().split())
    frogs.append((l, w, h))

# Call the function with input values
print(max_frogs_escape(n, d, frogs))
```
