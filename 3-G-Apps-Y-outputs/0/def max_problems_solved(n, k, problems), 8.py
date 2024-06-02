
def max_problems_solved(n, k, problems):
    left = 0
    right = n - 1
    solved = 0
    
    while left <= right:
        if problems[left] <= k:
            solved += 1
            left += 1
        elif problems[right] <= k:
            solved += 1
            right -= 1
        else:
            break
    
    return solved

# Input
n, k = map(int, input().split())
problems = list(map(int, input().split()))

# Output
print(max_problems_solved(n, k, problems))
