
def max_valid_segment_length(n, sushi_types):
    count = {1: 0, 2: 0}
    max_length = 0
    prefix_count = [{0: 0, 1: 0}, {0: 0, 1: 0}]

    for i in range(n):
        count[sushi_types[i]] += 1
        prefix_count[sushi_types[i] - 1][count[sushi_types[i]] % 2] = i + 1

        min_prefix = min(prefix_count[0][0], prefix_count[1][1])
        max_length = max(max_length, i - min_prefix)

    return max_length

# Read input
n = int(input())
sushi_types = list(map(int, input().split()))

# Call the function and print the result
print(max_valid_segment_length(n, sushi_types))
