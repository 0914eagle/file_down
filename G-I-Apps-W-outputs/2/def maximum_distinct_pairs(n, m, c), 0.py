
def maximum_distinct_pairs(n, m, c):
    pairs = {}
    for i in range(1, m+1):
        pairs[i] = []

    for idx, color in enumerate(c, start=1):
        pairs[color].append(idx)

    result = []
    max_distinct_pairs = min(len(pairs[1]), len(pairs[2]))
    
    for i in range(max_distinct_pairs):
        result.append((pairs[1][i], pairs[2][i]))

    print(max_distinct_pairs)
    for pair in result:
        print(pair[0], pair[1])

# Sample Input
n, m = 6, 3
c = [1, 3, 2, 2, 1, 1]
maximum_distinct_pairs(n, m, c)

n, m = 4, 2
c = [1, 2, 1, 1]
maximum_distinct_pairs(n, m, c)
```
