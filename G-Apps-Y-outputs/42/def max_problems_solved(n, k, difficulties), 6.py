
def max_problems_solved(n, k, difficulties):
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

# Read input
n, k = map(int, input().split())
difficulties = list(map(int, input().split()))

# Call the function and print the result
print(max_problems_solved(n, k, difficulties))