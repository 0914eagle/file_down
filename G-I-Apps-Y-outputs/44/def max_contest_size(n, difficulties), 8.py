
def max_contest_size(n, difficulties):
    max_contests = [1] * n  # Initialize array to store the maximum size of contest ending at each problem
    
    for i in range(n):
        for j in range(i):
            if difficulties[i] <= 2 * difficulties[j]:  # Check condition for contest validity
                max_contests[i] = max(max_contests[i], max_contests[j] + 1)
    
    return max(max_contests)


# Reading input
n = int(input())
difficulties = list(map(int, input().split()))

# Finding and printing the maximum size of the contest
result = max_contest_size(n, difficulties)
print(result)
```
