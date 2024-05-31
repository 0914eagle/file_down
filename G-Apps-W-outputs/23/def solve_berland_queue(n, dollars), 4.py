
def solve_berland_queue(n, dollars):
    dollars = dollars[::-1]
    result = []

    for i in range(n):
        result.append(max(dollars[i] - i, 1))

    for i in range(1, n):
        if result[i] < result[i-1]:
            return ":("

    return ' '.join(map(str, result[::-1]))

# Input
n = int(input())
dollars = list(map(int, input().split()))

# Output
print(solve_berland_queue(n, dollars))
