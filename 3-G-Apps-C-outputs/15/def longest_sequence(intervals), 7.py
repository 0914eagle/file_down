
def longest_sequence(intervals):
    intervals.sort(key=lambda x: x[0])
    dp = [1] * len(intervals)
    prev = [-1] * len(intervals)

    for i in range(1, len(intervals)):
        for j in range(i):
            if intervals[i][0] > intervals[j][0] and intervals[i][1] < intervals[j][1]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    max_length = max(dp)
    end_index = dp.index(max_length)
    result = []
    while end_index != -1:
        result.append(intervals[end_index])
        end_index = prev[end_index]

    return max_length, result[::-1]

# Read input
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
