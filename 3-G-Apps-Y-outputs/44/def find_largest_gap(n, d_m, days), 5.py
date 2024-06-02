
def find_largest_gap(n, d_m, days):
    for i in range(n):
        if days[i] <= d_m:
            if i == 0:
                return f"It hadn't snowed this early in {i} year!"
            else:
                return f"It hadn't snowed this early in {i} years!"
    return "It had never snowed this early!"

# Input
n, d_m = map(int, input().split())
days = list(map(int, input().split()))

# Output
print(find_largest_gap(n, d_m, days))
