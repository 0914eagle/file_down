
def max_frogs_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[0], reverse=True)  # Sort frogs by leap capacity in descending order
    dp = [0] * (d + 1)  # Initialize dynamic programming array

    for i in range(n):
        l, w, h = frogs[i]
        for j in range(d, h - 1, -1):
            if dp[j - h] + w <= l:  # Check if the frog can carry the weight
                dp[j] = max(dp[j], dp[j - h] + w)

    return max(dp)

# Input processing
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

# Output
print(max_frogs_escape(n, d, frogs))
