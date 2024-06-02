
def solve_problems(n, k, problems):
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

# Read input
n, k = map(int, input().split())
problems = list(map(int, input().split()))

# Call the function and print the result
print(solve_problems(n, k, problems))
