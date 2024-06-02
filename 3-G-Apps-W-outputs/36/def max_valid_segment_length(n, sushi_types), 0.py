
def max_valid_segment_length(n, sushi_types):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (1 if sushi_types[i - 1] == 1 else -1)

    first_occurrence = {}
    max_length = 0

    for i, prefix in enumerate(prefix_sum):
        if prefix not in first_occurrence:
            first_occurrence[prefix] = i
        else:
            max_length = max(max_length, i - first_occurrence[prefix])

    return max_length

# Read input
n = int(input())
sushi_types = list(map(int, input().split()))

# Call the function and print the result
print(max_valid_segment_length(n, sushi_types))
