
def determine_lineup(n, d):
    lineup = [1] + [0] * n
    for i in range(1, n):
        lineup[d[i-1]+i] = i + 1
    return lineup

# Input
n = int(input())
d = list(map(int, input().split()))

# Output
print(*determine_lineup(n, d))
