
def solve_problems(n, k, difficulties):
    left = 0
    right = n - 1
    solved = 0
    
    while left <= right:
        if difficulties[left] <= k:
            solved += 1
            left += 1
        elif difficulties[right] <= k:
            solved += 1
            right -= 1
        else:
            break
    
    return solved

# Input
n, k = map(int, input().split())
difficulties = list(map(int, input().split()))

# Output
print(solve_problems(n, k, difficulties))
