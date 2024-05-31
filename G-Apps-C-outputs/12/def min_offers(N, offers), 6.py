
def min_offers(N, offers):
    offers.sort(key=lambda x: (x[1], x[2]))  # Sort the offers by start section and then end section
    dp = [[float('inf')] * 4 for _ in range(10001)]  # Initialize a DP table with all sections and 4 colors

    for color, start, end in offers:
        for i in range(start, end + 1):
            dp[i][1] = min(dp[i][1], dp[i - 1][3] + 1)  # Update the DP table for 1 color
            dp[i][2] = min(dp[i][2], dp[i - 1][1] + 1)  # Update the DP table for 2 colors
            dp[i][3] = min(dp[i][3], min(dp[i - 1][1], dp[i - 1][2]) + 1)  # Update the DP table for 3 colors

    if dp[10000][3] == float('inf'):
        return "IMPOSSIBLE"
    else:
        return dp[10000][3]

# Input parsing
N = int(input())
offers = []
for _ in range(N):
    color, start, end = input().split()
    offers.append((color, int(start), int(end)))

# Call the function and print the result
print(min_offers(N, offers))
