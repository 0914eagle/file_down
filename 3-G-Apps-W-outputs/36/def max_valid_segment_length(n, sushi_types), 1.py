
def max_valid_segment_length(n, sushi_types):
    count = {1: 0, 2: 0}
    max_length = 0
    prefix_count = [{0: 0, 1: 0}]

    for t in sushi_types:
        count[t] += 1
        prefix_count.append(count.copy())

    for i in range(1, n + 1):
        for j in range(2):
            left_count = prefix_count[i][j] - prefix_count[i - 1][j]
            right_count = prefix_count[n][j] - prefix_count[i][j]
            max_length = max(max_length, min(left_count, right_count) * 2)

    return max_length

# Input reading
n = int(input())
sushi_types = list(map(int, input().split()))

# Call the function and print the result
print(max_valid_segment_length(n, sushi_types))
