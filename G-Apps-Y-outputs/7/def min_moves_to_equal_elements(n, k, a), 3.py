
def min_moves_to_equal_elements(n, k, a):
    counts = {}
    for num in a:
        counts[num] = counts.get(num, 0) + 1

    unique_nums = sorted(counts.keys())
    i = 0
    moves = 0
    while len(unique_nums) > k:
        if counts[unique_nums[i]] <= 1:
            i += 1
        else:
            diff1 = unique_nums[i + 1] - unique_nums[i]
            diff2 = unique_nums[-1] - unique_nums[i]
            if diff1 <= diff2:
                moves += counts[unique_nums[i]]
                counts[unique_nums[i + 1]] = counts.get(unique_nums[i + 1], 0) + counts[unique_nums[i]]
                counts[unique_nums[i]] = 0
                i += 1
            else:
                moves += counts[unique_nums[i]]
                counts[unique_nums[-1]] = counts.get(unique_nums[-1], 0) + counts[unique_nums[i]]
                counts[unique_nums[i]] = 0
        unique_nums = sorted(counts.keys())

    return moves

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function with input values
result = min_moves_to_equal_elements(n, k, a)

# Print the result
print(result)
