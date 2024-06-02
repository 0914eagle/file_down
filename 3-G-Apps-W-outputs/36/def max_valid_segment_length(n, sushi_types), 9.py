
def max_valid_segment_length(n, sushi_types):
    count_tuna = 0
    count_eel = 0
    max_length = 0
    prefix_counts = [(0, 0)]

    for t in sushi_types:
        if t == 1:
            count_tuna += 1
        else:
            count_eel += 1
        prefix_counts.append((count_tuna, count_eel))

    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            tuna_left, eel_left = prefix_counts[i]
            tuna_right, eel_right = prefix_counts[j]
            if abs(tuna_left - tuna_right) == abs(eel_left - eel_right):
                max_length = max(max_length, i - j)

    return max_length

# Read input
n = int(input())
sushi_types = list(map(int, input().split()))

# Call the function and print the output
print(max_valid_segment_length(n, sushi_types))
