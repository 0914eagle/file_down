
def sort_permutation(n, p):
    swaps = []
    for i in range(n):
        max_diff = -1
        max_diff_index = -1
        for j in range(i, n):
            if 2 * abs(i - j) >= n and p[j] == i + 1:
                max_diff = abs(i - j)
                max_diff_index = j
                break
        if max_diff_index != i:
            swaps.append((i + 1, max_diff_index + 1))
            p[i], p[max_diff_index] = p[max_diff_index], p[i]
    
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

# Input parsing
n = int(input())
p = list(map(int, input().split()))

# Call the function with the given input
sort_permutation(n, p)
```
