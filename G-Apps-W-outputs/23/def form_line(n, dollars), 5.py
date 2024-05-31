
def form_line(n, dollars):
    line = []
    for dollar in dollars:
        line.append([-dollar, dollar])

    line.sort()

    for i in range(n-1):
        if line[i][1] < line[i+1][1]:
            line[i], line[i+1] = line[i+1], line[i]
            line[i][1] += 1
            line[i+1][1] -= 1

    line.sort(key=lambda x: x[0])

    for i in range(n):
        dollars[i] = line[i][1]

    return dollars if all(dollars[i] <= dollars[i+1] for i in range(n-1)) else [":("]


# Input
n = int(input())
dollars = list(map(int, input().split()))

# Output
result = form_line(n, dollars)
print(" ".join(map(str, result)))
