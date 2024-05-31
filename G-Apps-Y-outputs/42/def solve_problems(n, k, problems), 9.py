
def solve_problems(n, k, problems):
    solved = 0
    left = 0
    right = n - 1

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
print(solve_problems(n, k, problems))