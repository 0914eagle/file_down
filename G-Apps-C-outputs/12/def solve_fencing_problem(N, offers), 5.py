
def solve_fencing_problem(N, offers):
    offers.sort(key=lambda x: (x[1], x[2]))
    
    dp = [float('inf')] * 10001
    dp[0] = 0
    
    for i in range(N):
        color, start, end = offers[i]
        for j in range(end, start - 1, -1):
            dp[j] = min(dp[j], dp[start - 1] + 1)
    
    if dp[10000] > 3:
        return "IMPOSSIBLE"
    else:
        return dp[10000]

# Input parsing
N = int(input())
offers = []
for _ in range(N):
    color, start, end = input().split()
    offers.append((color, int(start), int(end)))

# Call the function and print the result
result = solve_fencing_problem(N, offers)
print(result)
