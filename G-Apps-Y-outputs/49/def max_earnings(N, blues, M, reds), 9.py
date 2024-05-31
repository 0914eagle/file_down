
def max_earnings(N, blues, M, reds):
    max_earnings = 0
    for blue in blues:
        earnings = blues.count(blue) - reds.count(blue)
        if earnings > max_earnings:
            max_earnings = earnings
    return max_earnings

# Input
N = int(input())
blues = [input() for _ in range(N)]
M = int(input())
reds = [input() for _ in range(M)]

# Output
print(max_earnings(N, blues, M, reds))
