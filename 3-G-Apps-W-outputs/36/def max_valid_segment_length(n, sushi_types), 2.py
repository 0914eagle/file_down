
def max_valid_segment_length(n, sushi_types):
    prefix_sum = [0]
    for t in sushi_types:
        if t == 1:
            prefix_sum.append(prefix_sum[-1] + 1)
        else:
            prefix_sum.append(prefix_sum[-1] - 1)

    count = {}
    max_length = 0
    for i in range(n+1):
        if prefix_sum[i] not in count:
            count[prefix_sum[i]] = i
        else:
            max_length = max(max_length, i - count[prefix_sum[i]])

    return max_length

# Read input
n = int(input())
sushi_types = list(map(int, input().split()))

# Call the function and print the result
print(max_valid_segment_length(n, sushi_types))
