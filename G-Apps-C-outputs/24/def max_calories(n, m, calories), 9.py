
def max_calories(n, m, calories):
    dp = [[0] * (n + 1) for _ in range(3)]

    for i in range(1, n + 1):
        for j in range(1, 3):
            dp[j][i] = max(dp[j][i - 1], dp[j - 1][i - 1] + calories[i - 1])

    return dp[2][n]

# Input processing
input_line = input().strip().split()
n = int(input_line[0])
m = int(input_line[1])

calories = list(map(int, input().strip().split()))

result = max_calories(n, m, calories)
print(result)
