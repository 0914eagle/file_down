
def longest_sequence(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on the start value
    dp = [1] * len(intervals)  # Initialize dynamic programming array with 1 for each interval

    for i in range(1, len(intervals)):
        for j in range(i):
            if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    max_index = dp.index(max_length)

    result = [intervals[max_index]]
    current_length = max_length

    for i in range(max_index - 1, -1, -1):
        if dp[i] == current_length - 1 and intervals[i][0] <= result[-1][0] and intervals[i][1] >= result[-1][1]:
            result.append(intervals[i])
            current_length -= 1

    return max_length, result[::-1]

# Input processing
N = int(input())
intervals = []
for _ in range(N):
    A, B = map(int, input().split())
    intervals.append((A, B))

# Find the longest sequence
length, sequence = longest_sequence(intervals)

# Output the result
print(length)
for interval in sequence:
    print(interval[0], interval[1])
