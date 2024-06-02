
def longest_sequence(intervals):
    intervals.sort(key=lambda x: x[0])
    dp = [1] * len(intervals)
    prev = [-1] * len(intervals)
    max_len = 1
    max_idx = 0

    for i in range(1, len(intervals)):
        for j in range(i):
            if intervals[i][0] > intervals[j][0] and intervals[i][1] < intervals[j][1]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i

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

length, sequence = longest_sequence(intervals)

print(length)
for interval in sequence:
    print(interval[0], interval[1])
