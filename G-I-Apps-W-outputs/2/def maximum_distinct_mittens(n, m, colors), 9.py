
def maximum_distinct_mittens(n, m, colors):
    distinct_pairs = min(colors.count(i) for i in range(1, m+1))
    print(distinct_pairs * 2)
    
    left_mittens = [0] * n
    right_mittens = [0] * n

    for i in range(1, m+1):
        indices = [j for j, color in enumerate(colors) if color == i]

        for idx, j in enumerate(indices):
            left_mittens[j] = i
            right_mittens[j] = indices[(idx + 1) % len(indices)] + 1

    for left, right in zip(left_mittens, right_mittens):
        print(left, right)

n, m = map(int, input().split())
colors = list(map(int, input().split()))

maximum_distinct_mittens(n, m, colors)
```
