
def max_frogs_to_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[0], reverse=True)  # Sort frogs by leap capacity in descending order
    dp = [0] * (d + 1)  # Initialize a dynamic programming array to store the maximum number of frogs that can escape at each depth

    for frog in frogs:
        l, w, h = frog
        for i in range(d, h - 1, -1):
            if dp[i - h] + 1 > dp[i] and w + sum(f[1] for f in frogs if f[2] < h) <= w:
                dp[i] = dp[i - h] + 1

    return max(dp)

# Input parsing
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

print(max_frogs_to_escape(n, d, frogs))
