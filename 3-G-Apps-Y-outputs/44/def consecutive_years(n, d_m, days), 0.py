
def consecutive_years(n, d_m, days):
    for i in range(1, n):
        if days[i] <= d_m:
            if i == 1:
                return f"It hadn't snowed this early in {i-1} year!"
            else:
                return f"It hadn't snowed this early in {i-1} years!"
    return "It had never snowed this early!"

# Input parsing
n, d_m = map(int, input().split())
days = list(map(int, input().split()))

# Call the function with the input values
result = consecutive_years(n, d_m, days)
print(result)
