
def max_valid_segment_length(n, sushi_types):
    count = {1: 0, 2: 0}
    max_length = 0
    prefix_count = [{0: 0, 1: 0}]

    for t in sushi_types:
        count[t] += 1
        prefix_count.append(count.copy())

    for i in range(1, n + 1):
        left_tuna = prefix_count[i][1]
        left_eel = prefix_count[i][2]
        right_tuna = count[1] - left_tuna
        right_eel = count[2] - left_eel

        if left_tuna == left_eel or right_tuna == right_eel:
            max_length = max(max_length, i)

    return max_length

# Input
n = int(input())
sushi_types = list(map(int, input().split()))

# Output
print(max_valid_segment_length(n, sushi_types))
