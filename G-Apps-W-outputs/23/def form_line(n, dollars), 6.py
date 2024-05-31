
def form_line(n, dollars):
    dollars_sorted = sorted([(dollars[i], i) for i in range(n)])
    new_line = [0] * n
    total_dollars = sum(d for d, _ in dollars_sorted)

    for i in range(n):
        d, index = dollars_sorted[i]
        if d >= total_dollars:
            return ":("
        new_line[index] = total_dollars
        total_dollars -= d

    return " ".join(map(str, new_line))

# Input
n = int(input())
dollars = list(map(int, input().split()))

# Output
print(form_line(n, dollars))
