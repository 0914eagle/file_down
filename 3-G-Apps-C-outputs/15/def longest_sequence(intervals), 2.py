
def longest_sequence(intervals):
    intervals.sort(key=lambda x: x[0])
    n = len(intervals)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if intervals[i][0] > intervals[j][0] and intervals[i][1] < intervals[j][1]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    max_len = max(dp)
    max_idx = dp.index(max_len)

    result = []
    while max_idx != -1:
        result.append(intervals[max_idx])
        max_idx = prev[max_idx]

    return max_len, result[::-1]

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
