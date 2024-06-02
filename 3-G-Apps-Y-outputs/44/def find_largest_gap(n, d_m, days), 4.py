
def find_largest_gap(n, d_m, days):
    for i in range(1, n):
        if days[i] <= d_m:
            if i == 1:
                return f"It hadn't snowed this early in {i-1} year!"
            else:
                return f"It hadn't snowed this early in {i-1} years!"
    return "It had never snowed this early!"

# Read input
n, d_m = map(int, input().split())
days = list(map(int, input().split()))

# Call the function and print the result
result = find_largest_gap(n, d_m, days)
print(result)
